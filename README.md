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

# Handling comment replies

Each comment entry is printed with an ID starting with #1.
But For a reply the ID is in #X.Y format where X is the ID of the comment for which the reply was sent.

Check #5.1 in the example below.


# Example usage

```
$ git-github-pr-to-text --repository apache/spark 32083
------------------------------------------------------------------------------------
--- [SPARK-34886][PYTHON] Port/integrate Koalas DataFrame unit test into PySpark ---
------------------------------------------------------------------------------------
### What changes were proposed in this pull request?
Now that we merged the Koalas main code into the PySpark code base (#32036), we should port the Koalas DataFrame unit test to PySpark.

### Why are the changes needed?
Currently, the pandas-on-Spark modules are not tested at all. We should enable the DataFrame unit test first.

### Does this PR introduce _any_ user-facing change?
No.


### How was this patch tested?
Enable the DataFrame unit test.

-------------------------------------------------------------------------------------
--- #1  ueshin  https://github.com/apache/spark/pull/32083#issuecomment-815401615 ---
-------------------------------------------------------------------------------------
ok to test.

--------------------------------------------------------------------------------------
--- #2  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-815438615 ---
--------------------------------------------------------------------------------------
Kubernetes integration test unable to build dist.

exiting with code: 1
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41627/


--------------------------------------------------------------------------------------
--- #3  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-815496662 ---
--------------------------------------------------------------------------------------
**[Test build #137049 has finished](https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/137049/testReport)** for PR 32083 at commit [`3b924c0`](https://github.com/apache/spark/commit/3b924c01cc2e329ede64725a4aca9ffd1f37f44e).
 * This patch passes all tests.
 * This patch merges cleanly.
 * This patch adds no public classes.

------------------------------------------------------------------------------------------
--- #4  HyukjinKwon  https://github.com/apache/spark/pull/32083#issuecomment-815715229 ---
------------------------------------------------------------------------------------------
add to whitelist

-----------------------------------------------------------------------------------------
--- #5  HyukjinKwon  https://github.com/apache/spark/pull/32083#discussion_r609618007 ---
-----------------------------------------------------------------------------------------
path: python/pyspark/pandas/testing/utils.py:46
{{{
@@ -0,0 +1,423 @@
+#
+# Licensed to the Apache Software Foundation (ASF) under one or more
+# contributor license agreements.  See the NOTICE file distributed with
+# this work for additional information regarding copyright ownership.
+# The ASF licenses this file to You under the Apache License, Version 2.0
+# (the "License"); you may not use this file except in compliance with
+# the License.  You may obtain a copy of the License at
+#
+#    http://www.apache.org/licenses/LICENSE-2.0
+#
+# Unless required by applicable law or agreed to in writing, software
+# distributed under the License is distributed on an "AS IS" BASIS,
+# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
+# See the License for the specific language governing permissions and
+# limitations under the License.
+#
+
+import functools
+import shutil
+import tempfile
+import unittest
+import warnings
+from contextlib import contextmanager
+from distutils.version import LooseVersion
+
+import pandas as pd
+from pandas.api.types import is_list_like
+from pandas.testing import assert_frame_equal, assert_index_equal, assert_series_equal
+
+from pyspark import pandas as pp
+from pyspark.pandas.frame import DataFrame
+from pyspark.pandas.indexes import Index
+from pyspark.pandas.series import Series
+from pyspark.pandas.utils import default_session, sql_conf as sqlc, SPARK_CONF_ARROW_ENABLED
+
+
+class SQLTestUtils(object):
}}}
I think we have this util in PySpark. we should probably merge

--------------------------------------------------------------------------------------------------
--- #5.1  xinrong-databricks  https://github.com/apache/spark/pull/32083#discussion_r609970951 ---
--------------------------------------------------------------------------------------------------
path: python/pyspark/pandas/testing/utils.py:46
That's a good idea!

May I take it as a separate task later and port test files first?

--------------------------------------------------------------------------------------
--- #5.2  ueshin  https://github.com/apache/spark/pull/32083#discussion_r610140147 ---
--------------------------------------------------------------------------------------
path: python/pyspark/pandas/testing/utils.py:46
Shall we file a JIRA ticket to track the task then?

--------------------------------------------------------------------------------------------------
--- #5.3  xinrong-databricks  https://github.com/apache/spark/pull/32083#discussion_r610245020 ---
--------------------------------------------------------------------------------------------------
path: python/pyspark/pandas/testing/utils.py:46
Certainly, I filed https://issues.apache.org/jira/browse/SPARK-34999 to track this.

--------------------------------------------------------------------------------------
--- #6  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-815811284 ---
--------------------------------------------------------------------------------------
Kubernetes integration test starting
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41654/


--------------------------------------------------------------------------------------
--- #7  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-815811299 ---
--------------------------------------------------------------------------------------
Kubernetes integration test status failure
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41654/


--------------------------------------------------------------------------------------
--- #8  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-815883037 ---
--------------------------------------------------------------------------------------
**[Test build #137076 has finished](https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/137076/testReport)** for PR 32083 at commit [`3b924c0`](https://github.com/apache/spark/commit/3b924c01cc2e329ede64725a4aca9ffd1f37f44e).
 * This patch passes all tests.
 * This patch merges cleanly.
 * This patch adds no public classes.

--------------------------------------------------------------------------------------
--- #9  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-815999060 ---
--------------------------------------------------------------------------------------
**[Test build #137092 has finished](https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/137092/testReport)** for PR 32083 at commit [`6d13af9`](https://github.com/apache/spark/commit/6d13af9d42386c9b7c7be902b7fd4a01876fc350).
 * This patch **fails Python style tests**.
 * This patch merges cleanly.
 * This patch adds no public classes.

---------------------------------------------------------------------------------------
--- #10  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816036878 ---
---------------------------------------------------------------------------------------
Kubernetes integration test starting
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41670/


---------------------------------------------------------------------------------------
--- #11  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816036895 ---
---------------------------------------------------------------------------------------
Kubernetes integration test status failure
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41670/


---------------------------------------------------------------------------------------
--- #12  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816145122 ---
---------------------------------------------------------------------------------------
Kubernetes integration test unable to build dist.

exiting with code: 1
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41675/


--------------------------------------------------------------------------------------
--- #13  ueshin  https://github.com/apache/spark/pull/32083#issuecomment-816215100 ---
--------------------------------------------------------------------------------------
I guess we should add `pyspark.pandas.tests` to `heavy_tests` in `python/run-tests.py`?

---------------------------------------------------------------------------------------
--- #14  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816258196 ---
---------------------------------------------------------------------------------------
**[Test build #137097 has finished](https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/137097/testReport)** for PR 32083 at commit [`4abe527`](https://github.com/apache/spark/commit/4abe52758509ef23e3e8241fb4389195c9b39186).
 * This patch passes all tests.
 * This patch merges cleanly.
 * This patch adds no public classes.

---------------------------------------------------------------------------------------
--- #15  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816274287 ---
---------------------------------------------------------------------------------------
Kubernetes integration test starting
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41678/


---------------------------------------------------------------------------------------
--- #16  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816274294 ---
---------------------------------------------------------------------------------------
Kubernetes integration test status failure
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41678/


---------------------------------------------------------------------------------------
--- #17  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816327818 ---
---------------------------------------------------------------------------------------
**[Test build #137100 has finished](https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/137100/testReport)** for PR 32083 at commit [`3a73eba`](https://github.com/apache/spark/commit/3a73ebad0a3042f071407420f1606e39bcb3965b).
 * This patch passes all tests.
 * This patch merges cleanly.
 * This patch adds no public classes.

---------------------------------------------------------------------------------------
--- #18  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816339977 ---
---------------------------------------------------------------------------------------
Kubernetes integration test starting
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41685/


---------------------------------------------------------------------------------------
--- #19  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816339986 ---
---------------------------------------------------------------------------------------
Kubernetes integration test status failure
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41685/


---------------------------------------------------------------------------------------
--- #20  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816373005 ---
---------------------------------------------------------------------------------------
**[Test build #137107 has finished](https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/137107/testReport)** for PR 32083 at commit [`f5d9fd3`](https://github.com/apache/spark/commit/f5d9fd387da89b5650b05dc69143efed971255ac).
 * This patch **fails Spark unit tests**.
 * This patch merges cleanly.
 * This patch adds no public classes.

-------------------------------------------------------------------------------------------
--- #21  HyukjinKwon  https://github.com/apache/spark/pull/32083#issuecomment-816382559 ---
-------------------------------------------------------------------------------------------
retest this please

---------------------------------------------------------------------------------------
--- #22  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816407146 ---
---------------------------------------------------------------------------------------
Kubernetes integration test starting
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41692/


---------------------------------------------------------------------------------------
--- #23  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816408685 ---
---------------------------------------------------------------------------------------
Kubernetes integration test status failure
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41692/


---------------------------------------------------------------------------------------
--- #24  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816437788 ---
---------------------------------------------------------------------------------------
**[Test build #137113 has finished](https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/137113/testReport)** for PR 32083 at commit [`f5d9fd3`](https://github.com/apache/spark/commit/f5d9fd387da89b5650b05dc69143efed971255ac).
 * This patch **fails Spark unit tests**.
 * This patch merges cleanly.
 * This patch adds no public classes.

-------------------------------------------------------------------------------------------
--- #25  HyukjinKwon  https://github.com/apache/spark/pull/32083#issuecomment-816445245 ---
-------------------------------------------------------------------------------------------
retest this please

-------------------------------------------------------------------------------------------
--- #26  HyukjinKwon  https://github.com/apache/spark/pull/32083#issuecomment-816453998 ---
-------------------------------------------------------------------------------------------
I manually checked that all related tests passed during running multiple times. I don't believe this cause any extra test failures.

Merged to master.

---------------------------------------------------------------------------------------
--- #27  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816503736 ---
---------------------------------------------------------------------------------------
Kubernetes integration test starting
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41698/


---------------------------------------------------------------------------------------
--- #28  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816510009 ---
---------------------------------------------------------------------------------------
Kubernetes integration test status failure
URL: https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder-K8s/41698/


---------------------------------------------------------------------------------------
--- #29  SparkQA  https://github.com/apache/spark/pull/32083#issuecomment-816557089 ---
---------------------------------------------------------------------------------------
**[Test build #137119 has finished](https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/137119/testReport)** for PR 32083 at commit [`f5d9fd3`](https://github.com/apache/spark/commit/f5d9fd387da89b5650b05dc69143efed971255ac).
 * This patch passes all tests.
 * This patch merges cleanly.
 * This patch adds no public classes.


vim: foldmethod=marker
```
