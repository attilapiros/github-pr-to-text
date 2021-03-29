#!/usr/bin/env python
from github import Github
import configparser
import os
import sys
import argparse

win_eol = '\r\n'
unix_eol = '\n'
code_start = '{{{'
code_end = '}}}'


def append_bordered(str_list, text):
    text = '--- ' + text + ' ---'
    border_len = len(text)
    separator = '-' * border_len
    str_list.append(separator)
    str_list.append(text)
    str_list.append(separator)


def entry_to_string(entry, withdiff, is_top):
    if is_top:
        prefix = ''
    else:
        prefix = '> '

    str_list = []

    # header
    text = '#' + str(entry['id']) + '  '
    if entry['in_reply_to_id'] is not None:
        text = text + "(reply to: #" + str(entry['in_reply_to_id']) + ')  '
    text = text + entry['user_login'] + '  '
    text = text + entry['url']
    append_bordered(str_list, text)

    # add file path
    if entry['path'] is not None:
        str_list.append('path: ' + entry['path'])
    # add code diff if given and configured by arg
    if withdiff and entry['code_diff'] is not None:
        str_list.append(code_start + '\n' +
                        entry['code_diff'] + '\n' + code_end)
    # the body of the comment
    str_list.extend(entry['body'].split('\n'))

    return prefix + ('\n' + prefix).join(str_list) + '\n'


def build_review_comment_hiearchy(review_comments):
    rootEntriesById = {}
    leaves = []
    for review_comment in review_comments:
        entryId = review_comment.id
        in_reply_to_id = review_comment.in_reply_to_id
        entry = {
            'id': entryId,
            'in_reply_to_id': in_reply_to_id,
            'created_at': review_comment.created_at,
            'user_login': review_comment.user.login,
            'url': review_comment.html_url,
            'code_diff': review_comment.diff_hunk,
            'path': review_comment.path +
            ((':' + str(review_comment.position))
             if review_comment.position is not None else ''),
            'body': review_comment.body.replace(win_eol, unix_eol)
        }
        if in_reply_to_id is None:
            entry['replies'] = []
            rootEntriesById[entryId] = entry
        else:
            entry['code_diff'] = None
            leaves.append(entry)

    # print(rootEntriesById)

    for leave in leaves:
        rootEntriesById[leave['in_reply_to_id']]['replies'].append(leave)

    for root in rootEntriesById.values():
        root['replies'].sort(key=lambda e: e['created_at'])

    return list(rootEntriesById.values())


def process_issue_comments(issue_comments):
    entries = []
    for issue_comment in issue_comments:
        entryId = 'issue_comment_' + str(issue_comment.id)
        entries.append({
            'id': entryId,
            'in_reply_to_id': None,
            'created_at': issue_comment.created_at,
            'user_login': issue_comment.user.login,
            'url': issue_comment.html_url,
            'code_diff': None,
            'path': None,
            'body': issue_comment.body.replace(win_eol, unix_eol),
            'replies': []
        })
    return entries


def print_pr_title_and_description(pr):
    str_list = []
    append_bordered(str_list, pr.title)
    str_list.append(pr.body.replace(win_eol, unix_eol))

    for line in str_list:
        print(line)


def main(argv=None, apply_config=True):
    """Command-line entry."""
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(
        description='Download github PR comments.')
    parser.add_argument('--repository',
                        help='the Github repo name (default: %(default)s)',
                        default='apache/spark')
    parser.add_argument('--withdiff',
                        type=bool,
                        help='flag to switch off diffs (default: %(default)s)',
                        default=True)
    parser.add_argument('pr', type=int, help='the PR id')

    args = parser.parse_args(argv[1:])

    config = configparser.ConfigParser()
    config.read([os.path.expanduser('~/.github_access_token.cfg')])

    github = Github(config['github.com']['AccessToken'])
    repo = github.get_repo(args.repository)
    pr = repo.get_pull(args.pr)

    entries = build_review_comment_hiearchy(pr.get_review_comments())
    entries.extend(process_issue_comments(pr.get_issue_comments()))
    entries.sort(key=lambda e: e['created_at'])

    print_pr_title_and_description(pr)
    # print PR review and issue comments
    for entry in entries:
        print(entry_to_string(entry, args.withdiff, True))
        for reply in entry['replies']:
            print(entry_to_string(reply, args.withdiff, False))

    print('\nvim: foldmethod=marker')


if __name__ == '__main__':
    sys.exit(main())
