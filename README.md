# Known Issue: End of Line (EOL) on different Operating Systems (OSs)
## Description
On Mac and Linux, EOL is `\LF`; while on Windows, EOL is `\CRLF` by default.
Current docker image can only deal with EOL `\LF`, not `\CRLF`, and produces the following error, which is not human interpretable:
<img width="1100" alt="image" src="https://github.com/user-attachments/assets/c8fedb87-6630-4c06-9c3a-0c1ad525331b">

## Proposed Actions
### Documentation
We need to document this issue in the tutorials: [Computational Co-Design](https://storage.zuper.ai/sync/zupermind/mcdp-book/z7-prod/test/last/test-job/public.pdf)
### Temporary: rely on IDE (Thanks to @Meshal Alharbi for the solution)
On some IDEs, for example VSCode, we can choose EOL manually for each file:
<img width="664" alt="image" src="https://github.com/user-attachments/assets/b5dc661b-1f08-4a9f-b478-ceaf6760edcd">
### Good solution: set Docker Image/Every MCDP Repo to be robust
For Docker images, found this solution: [Docker for Windows: Dealing With Windows Line Endings](https://willi.am/blog/2016/08/11/docker-for-windows-dealing-with-windows-line-endings/)
But one needs to modify the image to test if it works.

For Repos, we can use `.gitattributes` file to force all files with EOL `\LF`. Reference: [https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings)
We can add it into the tutorials, too.
