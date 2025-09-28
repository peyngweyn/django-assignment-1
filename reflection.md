# Reflection

Setting up my Django environment was both a challenge and a valuable learning experience. One of the first issues I encountered was getting the virtual environment to work properly. Initially, I was unsure how to activate it in PowerShell, but I learned that I needed to run the correct script (`.\venv\Scripts\Activate.ps1`) to make sure the environment was active before installing packages.

Another major challenge was that my project was missing the `manage.py` file. This caused errors whenever I tried to run `python manage.py runserver` or `migrate`. I resolved this by rebuilding the project structure correctly, ensuring that `manage.py` and the necessary Django files were included. This taught me the importance of having the proper directory structure for Django.

Finally, I had some trouble pushing my project to GitHub. At first, I added the remote incorrectly, but by removing it and adding the correct repository URL, I was able to successfully push my code. Through these steps, I not only completed the setup but also gained confidence in debugging and problem-solving within a development workflow.
