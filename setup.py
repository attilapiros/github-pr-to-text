from setuptools import setup

setup(name='github-pr-to-text',
      version='0.1',
      description='Get the GitHub PR content in text format',
      url='http://github.com/attilapiros/github-pr-to-text',
      author='Atila Zsolt Piros',
      author_email='piros.attila.zsolt@gmail.com',
      license='Apache License 2.0',
      install_requires=[
          'PyGithub>=2.3.0',
      ],
      py_modules=['git_github_pr_to_text'],
      zip_safe=False,
      entry_points={'console_scripts': ['git-github-pr-to-text=git_github_pr_to_text:main']})
