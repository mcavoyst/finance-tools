from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="finance-tools",
        packages=find_packages(),
        package_data={
            "finance_tools": ["data/*", "example/*"]
        },
        entry_points={
            "console_scripts": [
                "finance-tools=finance_tools.main:main",
            ],
        },
    )