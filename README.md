# github-pr-to-text

Get the GitHub PR content in text format.

- Have you ever been annoyed by "hidden items" like this?
  ![Hidden items](doc/hidden_items_in_github_pr.png)
- Have you ever expanded several levels of collapsed comments just to search for a simple text in a GitHub PR?
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
$ git-github-pr-to-text --repository apache/spark 31999
---------------------------------------------------------------
--- Add column names to column number mismatch runtimeerror ---
---------------------------------------------------------------
### What changes were proposed in this pull request?
Adds names of columns returned by function to error message.
Change suggested here http://apache-spark-user-list.1001560.n3.nabble.com/Error-Message-Suggestion-td39884.html


### Why are the changes needed?
In the error message, the number of returned columns and number of expected columns are returned, but with the names of the actual columns returned, the error would be much more helpful and easier to debug.


### Does this PR introduce _any_ user-facing change?
Users would see the changed error when developing.


### How was this patch tested?
No new tests. Passes related tests on my machine.

------------------------------------------------------------------------------------------------------------------
--- #issue_comment_809741800  AmplabJenkins  https://github.com/apache/spark/pull/31999#issuecomment-809741800 ---
------------------------------------------------------------------------------------------------------------------
Can one of the admins verify this patch?

-------------------------------------------------------------------------------------------
--- #607907149  Yikun  https://github.com/apache/spark/pull/31999#discussion_r607907149 ---
-------------------------------------------------------------------------------------------
path: python/pyspark/worker.py:5
{{{
@@ -141,7 +141,8 @@ def wrapped(left_key_series, left_value_series, right_key_series, right_value_se
             raise RuntimeError(
                 "Number of columns of the returned pandas.DataFrame "
                 "doesn't match specified schema. "
-                "Expected: {} Actual: {}".format(len(return_type), len(result.columns)))
+                "Expected: {} Actual: {}"
}}}
`​``suggestion
                "Expected: {} Actual: {} "
`​``


vim: foldmethod=marker
```
