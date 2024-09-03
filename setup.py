import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"  # Changed to a single equals sign

REPO_NAME = "Chicken-Doctor"
AUTHOR_USER_NAME = "aviralsoni22"
SRC_REPO = "Chicken Doctor"
AUTHOR_EMAIL = "aviralsoni22@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package used in CNN app", 
    long_description=long_description,
    long_description_content_type="text/markdown", 
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"}, 
    packages=setuptools.find_packages(where="src")  # Corrected from "scr" to "src"
)
