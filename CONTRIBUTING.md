# Contributing to chitchat-dataset

1. Write code
   - We follow [PEP8] & the [Google Python Style Guide].
   - We use [black] to format all of our code. Always.
1. Write a [good](https://chris.beams.io/posts/git-commit/#seven-rules) commit message(s)
1. Open a pull request

Thank you! :tada:

## releasing

1. Bump the version (see `poetry help version` for more info):

   ```bash
   make release version=minor
   ```

1. Push the new tag and the [GitHub workflow] automatically should build the
   package and upload it to pypi.org:

   ```
   git push --follow-tags
   ```

[pep8]: https://www.python.org/dev/peps/pep-0008/
[google python style guide]: https://google.github.io/styleguide/pyguide.html
[black]: https://github.com/psf/black
[github workflow]: https://github.com/BYU-PCCL/chitchat-dataset/actions
