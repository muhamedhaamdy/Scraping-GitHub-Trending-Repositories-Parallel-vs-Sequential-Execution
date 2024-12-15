import requests
from bs4 import BeautifulSoup
import time  # For measuring execution time

# Function to scrape trending repositories for a given language
def scrape_trending(language):
    url = f"https://github.com/trending/{language}?since=daily"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        repos = soup.find_all("h2", class_="h3 lh-condensed")
        if repos:
            repo_titles = [repo.text.strip().replace('\n', ' ') for repo in repos]
            return {language: repo_titles}
        else:
            return {language: "No repositories found. Check the HTML structure."}
    else:
        return {language: f"Failed to fetch (Status code: {response.status_code})"}

# List of programming languages to scrape
languages = ["python", "javascript", "java", "c++", "go"]

# Sequential Execution
def sequential_execution():
    results = []
    for language in languages:
        results.append(scrape_trending(language))
    return results

if __name__ == "__main__":
    print("Running Sequential Execution...")
    start_time = time.time()
    results = sequential_execution()
    end_time = time.time()
    sequential_time = end_time - start_time

    for result in results:
        for language, repos in result.items():
            print(f"\nTrending repositories in {language.capitalize()}:\n")
            if isinstance(repos, list):
                for i, repo in enumerate(repos, 1):
                    print(f"{i}. {repo}")
            else:
                print(repos)

    print(f"\nSequential Execution Time: {sequential_time:.2f} seconds")

