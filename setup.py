from setuptools import find_packages, setup
from pathlib import Path
from typing import List


def get_requirements(file_path: str) -> List[str]:
    try:
        requirements_list = []
        with open(file_path, "r") as file:
            requirements = file.readlines()
            for requirement in requirements:
                requirement = requirement.strip()
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)
        return requirements_list
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while reading {file_path}: {e}")


setup(
    name="lungsxrayclassifier",
    version="0.0.1",
    author="Mohammad Shuaib",
    author_email="mohammadshuaib3455@gmail.com",
    description="Designed and implemented a deep learning model to classify lung X-ray images into categories such as healthy or diseased. The model leverages convolutional neural networks (CNNs) to detect conditions like pneumonia, tuberculosis, and COVID-19. Achieved high accuracy through rigorous data preprocessing, augmentation, and fine-tuning of the model. This project demonstrates the application of AI in healthcare to assist in early and precise diagnosis.",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
