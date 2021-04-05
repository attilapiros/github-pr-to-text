# github-pr-to-text

Get the GitHub PR content in text format.

- Have you ever disturbed by "hidden items" like this?
  ![Hidden items](doc/hidden_items_in_github_pr.png)
- Have you ever expanded several levels of collapsed comments just to search for a text in a GitHub PR?
- Have you ever missed your IDE/editor to visit an exact line within the code to which the comment was referring to?

If yes you can give a shot to this simple tool.

# Install

After cloning this repo call `pip install .` in the root directory of your clone.

# Setup

Create a github access token and add it to `~/.github_access_token.cfg` file like:

```
[github.com]
AccessToken = <your-github-access-token>
```

# Example usage

```
$ git-github-pr-to-text --repository apache/spark 31790
-----------------------------------------------------------------------------------------
--- [WIP][SPARK-34509][K8S] Make dynamic allocation upscaling more progressive on K8S ---
-----------------------------------------------------------------------------------------
This is a work in progress PR as I first would like test this solution extensively on a real k8s cluster not only with unit tests.

### What changes were proposed in this pull request?

Making upscaling more progressive to eagerly go up to the configured allocation batch size.

### Why are the changes needed?

The current solution will stops requesting PODS when even one POD request is active form the current batch.
After this PR allocation goes up to batch size as early as possible. My reasoning is the following: when POD allocation takes a long time then let's request as soon as possible, excess requests will be deleted anyway by downscaling.

### Does this PR introduce _any_ user-facing change?

No.

### How was this patch tested?

Existing unit test.
------------------------------------------------------------------------------------------------------------
--- #issue_comment_794487955  SparkQA  https://github.com/apache/spark/pull/31790#issuecomment-794487955 ---
------------------------------------------------------------------------------------------------------------
**[Test build #135910 has finished](https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/135910/testReport)** for PR 31790 at commit [`77a5c68`](https://github.com/apache/spark/commit/77a5c68bda296723c992c0d3c37a58eab5167a19).
 * This patch passes all tests.
 * This patch merges cleanly.
 * This patch adds no public classes.

------------------------------------------------------------------------------------------------------------
--- #issue_comment_794517255  SparkQA  https://github.com/apache/spark/pull/31790#issuecomment-794517255 ---
------------------------------------------------------------------------------------------------------------
Kubernetes integration test starting
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/40493/


------------------------------------------------------------------------------------------------------------
--- #issue_comment_794524004  SparkQA  https://github.com/apache/spark/pull/31790#issuecomment-794524004 ---
------------------------------------------------------------------------------------------------------------
Kubernetes integration test status failure
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/40493/



vim: foldmethod=marker
```
