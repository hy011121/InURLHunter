import yagooglesearch

# read
def load_dorks(filename):
    with open(filename, 'r') as file:
        dorks = [line.strip() for line in file if line.strip()]
    return dorks
def search_dorks(dorks):
    all_urls = []
    
    for dork in dorks:
        print(f"Searching for dork: {dork}")
        
        client = yagooglesearch.SearchClient(
            dork,
            tbs="li:1",
            max_search_result_urls_to_return=100,
            http_429_cool_off_time_in_minutes=45,
            http_429_cool_off_factor=1.5,
            verbosity=5,
            verbose_output=True,
        )
        client.assign_random_user_agent()
        
        search_results = client.search()
        for result in search_results:
            if 'url' in result:
                all_urls.append(result['url'])
    
    return all_urls
def save_to_file(urls, filename):
    with open(filename, 'w') as file:
        for url in urls:
            file.write(f"{url}\n")
    print(f"Saved {len(urls)} URLs to {filename}")
dorks_file = 'dork.txt'
urls_file = 'list.txt'
dorks = load_dorks(dorks_file)
urls = search_dorks(dorks)
save_to_file(urls, urls_file)
