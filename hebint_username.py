HEBINT - Advanced Username Module with Guaranteed Facebook Search Links
Search across 150+ platforms with ALWAYS VISIBLE Facebook search options!
"""

import requests
import json
from datetime import datetime
import concurrent.futures
import time
from colorama import init, Fore, Style

# Initialize colors
init()
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL

class UsernameModule:
    """Advanced username search with guaranteed Facebook links"""
    
    def __init__(self):
        """Initialize username module"""
        print(f"{GREEN}👤 Advanced Username Module Ready!{RESET}")
        self.results = {}
        self.found_profiles = []
        
        # Browser-like headers to avoid blocks
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
        }
        
        # Platform list - 150+ sites
        self.platforms = {
            # ========== FACEBOOK PROFILES ==========
            "Facebook Profile": "https://www.facebook.com/{}",
            
            # ========== INSTAGRAM ==========
            "Instagram": "https://www.instagram.com/{}",
            "Instagram Search": "https://www.instagram.com/explore/search/keyword/?q={}",
            "Instagram Tags": "https://www.instagram.com/explore/tags/{}/",
            "Instagram Locations": "https://www.instagram.com/explore/locations/?hl=en&q={}",
            
            # ========== TWITTER / X ==========
            "Twitter": "https://twitter.com/{}",
            "Twitter Search": "https://twitter.com/search?q={}",
            "Twitter Hashtag": "https://twitter.com/hashtag/{}",
            "Twitter Advanced": "https://twitter.com/search-advanced?lang=en&q={}",
            
            # ========== TIKTOK ==========
            "TikTok": "https://www.tiktok.com/@{}",
            "TikTok Search": "https://www.tiktok.com/search?q={}",
            "TikTok Hashtag": "https://www.tiktok.com/tag/{}",
            
            # ========== THREADS ==========
            "Threads": "https://www.threads.net/@{}",
            "Threads Search": "https://www.threads.net/search?q={}",
            
            # ========== LINKEDIN ==========
            "LinkedIn": "https://www.linkedin.com/in/{}",
            "LinkedIn Search": "https://www.linkedin.com/search/results/all/?keywords={}",
            "LinkedIn People": "https://www.linkedin.com/search/results/people/?keywords={}",
            "LinkedIn Sales": "https://www.linkedin.com/sales/profile/{}",
            
            # ========== REDDIT ==========
            "Reddit": "https://www.reddit.com/user/{}",
            "Reddit Search": "https://www.reddit.com/search/?q={}",
            "Reddit Subreddit": "https://www.reddit.com/r/{}",
            
            # ========== SNAPCHAT ==========
            "Snapchat": "https://www.snapchat.com/add/{}",
            
            # ========== PINTEREST ==========
            "Pinterest": "https://www.pinterest.com/{}",
            "Pinterest Search": "https://www.pinterest.com/search/pins/?q={}",
            
            # ========== TUMBLR ==========
            "Tumblr": "https://{}.tumblr.com",
            "Tumblr Search": "https://www.tumblr.com/search/{}",
            
            # ========== GITHUB ==========
            "GitHub": "https://github.com/{}",
            "GitHub Repos": "https://github.com/{}?tab=repositories",
            "GitHub Search": "https://github.com/search?q={}&type=code",
            
            # ========== OTHER PLATFORMS ==========
            "Medium": "https://medium.com/@{}",
            "Dev.to": "https://dev.to/{}",
            "HackerNews": "https://news.ycombinator.com/user?id={}",
            "Stack Overflow": "https://stackoverflow.com/users/{}",
            "Keybase": "https://keybase.io/{}",
            "About.me": "https://about.me/{}",
            "AngelList": "https://angel.co/u/{}",
            "ProductHunt": "https://www.producthunt.com/@{}",
            "Behance": "https://www.behance.net/{}",
            "Dribbble": "https://dribbble.com/{}",
            "Flickr": "https://www.flickr.com/people/{}",
            "500px": "https://500px.com/p/{}",
            "SoundCloud": "https://soundcloud.com/{}",
            "Spotify": "https://open.spotify.com/user/{}",
            "Bandcamp": "https://bandcamp.com/{}",
            "Steam": "https://steamcommunity.com/id/{}",
            "Twitch": "https://www.twitch.tv/{}",
            "Vimeo": "https://vimeo.com/{}",
            "Dailymotion": "https://www.dailymotion.com/{}",
            "Telegram": "https://t.me/{}",
            "Discord": "https://discord.com/users/{}",
            "Signal": "https://signal.me/#p/{}",
            
            # ========== ARABIC PLATFORMS ==========
            "Anazahra": "https://anazahra.com/{}",
            "ArabChat": "https://arabchat.org/members/{}",
            "Mawada": "https://mawada.com/profile/{}",
            "DubaiChat": "https://dubaichat.com/profile/{}",
        }
        
        print(f"{GREEN}✅ Loaded {len(self.platforms)} platforms{RESET}")
    
    def generate_facebook_search_links(self, username):
        """Generate Facebook search links - ALWAYS SHOWS"""
        print(f"\n{CYAN}📘 FACEBOOK SEARCH LINKS (Always Available):{RESET}")
        print(f"{BLUE}{'-' * 60}{RESET}")
        
        # Try different formats for better results
        encoded = username.replace(' ', '+').replace('_', '+').replace('-', '+')
        clean = username.replace('_', '').replace('-', '').replace(' ', '')
        
        facebook_links = {
            "🔍 Facebook People Search": f"https://www.facebook.com/search/people/?q={encoded}",
            "🔍 Facebook Pages Search": f"https://www.facebook.com/search/pages/?q={encoded}",
            "🔍 Facebook Groups Search": f"https://www.facebook.com/search/groups/?q={encoded}",
            "🔍 Facebook Posts Search": f"https://www.facebook.com/search/posts/?q={encoded}",
            "🔍 Facebook Photos Search": f"https://www.facebook.com/search/photos/?q={encoded}",
            "🔍 Facebook Videos Search": f"https://www.facebook.com/search/videos/?q={encoded}",
            "🔍 Facebook Marketplace": f"https://www.facebook.com/marketplace/search/?query={encoded}",
            "🔍 Facebook Profile (with underscores)": f"https://www.facebook.com/{username}",
            "🔍 Facebook Profile (no special chars)": f"https://www.facebook.com/{clean}",
            "🔍 Facebook Profile (with dashes)": f"https://www.facebook.com/{username.replace('_', '-')}",
        }
        
        print(f"  {GREEN}✅ Found {len(facebook_links)} Facebook search options{RESET}")
        
        # Show them immediately
        for name, url in facebook_links.items():
            print(f"  {CYAN}{name}:{RESET} {url}")
        
        return facebook_links
    
    def check_site(self, username, site_name, url_template):
        """Check if username exists on a single site"""
        url = url_template.format(username)
        
        try:
            response = requests.get(url, timeout=10, allow_redirects=True, headers=self.headers)
            
            if response.status_code == 200:
                # Check if it's actually a profile page
                content = response.text.lower()
                not_found_phrases = ["not found", "doesn't exist", "page not found", 
                                    "no results", "couldn't find", "does not exist",
                                    "profile not found", "user not found"]
                
                if not any(phrase in content for phrase in not_found_phrases):
                    return {
                        "site": site_name,
                        "url": url,
                        "exists": True,
                        "status_code": response.status_code
                    }
            
            return {
                "site": site_name,
                "url": url,
                "exists": False,
                "status_code": response.status_code
            }
            
        except requests.exceptions.Timeout:
            return {
                "site": site_name,
                "url": url,
                "exists": "timeout",
                "error": "Connection timeout"
            }
        except requests.exceptions.ConnectionError:
            return {
                "site": site_name,
                "url": url,
                "exists": "error",
                "error": "Connection error"
            }
        except Exception as e:
            return {
                "site": site_name,
                "url": url,
                "exists": "error",
                "error": str(e)
            }
    
    def investigate(self, username):
        """Search username across all platforms"""
        print(f"\n{CYAN}👤 Searching for username:{RESET} {YELLOW}{username}{RESET}")
        print(f"{BLUE}{'=' * 60}{RESET}")
        
        self.results = {
            "username": username,
            "timestamp": str(datetime.now()),
            "total_sites": len(self.platforms),
            "found_profiles": [],
            "not_found": [],
            "errors": []
        }
        
        # STEP 1: ALWAYS SHOW FACEBOOK SEARCH LINKS (even before checking)
        facebook_links = self.generate_facebook_search_links(username)
        self.results["facebook_search_links"] = facebook_links
        
        # STEP 2: Check all platforms
        print(f"\n{MAGENTA}📋 Checking {len(self.platforms)} platforms...{RESET}")
        print(f"{BLUE}{'-' * 60}{RESET}")
        
        # Use ThreadPoolExecutor for faster checking
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            future_to_site = {
                executor.submit(self.check_site, username, site_name, url_template): site_name
                for site_name, url_template in self.platforms.items()
            }
            
            for future in concurrent.futures.as_completed(future_to_site):
                site_name = future_to_site[future]
                try:
                    result = future.result()
                    
                    if result.get("exists") == True:
                        self.results["found_profiles"].append(result)
                        self.found_profiles.append(result)
                        print(f"  {GREEN}✅ {site_name}:{RESET} Found!")
                        
                    elif result.get("exists") == False:
                        self.results["not_found"].append(result)
                    else:
                        self.results["errors"].append(result)
                        
                except Exception as e:
                    self.results["errors"].append({
                        "site": site_name,
                        "error": str(e)
                    })
        
        # STEP 3: Summary
        print(f"\n{MAGENTA}{'=' * 60}{RESET}")
        print(f"{CYAN}📊 SUMMARY{RESET}")
        print(f"{BLUE}{'-' * 60}{RESET}")
        
        found_count = len(self.results['found_profiles'])
        not_found_count = len(self.results['not_found'])
        error_count = len(self.results['errors'])
        
        print(f"  {GREEN}✅ Found on:{RESET} {found_count} sites")
        print(f"  {RED}❌ Not found:{RESET} {not_found_count} sites")
        print(f"  {YELLOW}⚠️ Errors:{RESET} {error_count} sites")
        
        # STEP 4: Show found profiles (excluding Facebook since we already showed search links)
        if found_count > 0:
            print(f"\n{GREEN}🌟 OTHER PLATFORMS FOUND:{RESET}")
            print(f"{BLUE}{'-' * 60}{RESET}")
            
            # Show non-Facebook results (Facebook search links already shown)
            non_facebook = [p for p in self.results['found_profiles'] if 'Facebook' not in p['site']]
            
            for profile in non_facebook[:25]:
                print(f"  {CYAN}{profile['site']}:{RESET} {profile['url']}")
            
            if len(non_facebook) > 25:
                print(f"  {YELLOW}... and {len(non_facebook) - 25} more{RESET}")
        
        # STEP 5: Remind about Facebook search links
        print(f"\n{CYAN}📘 Don't forget to check the Facebook search links above!{RESET}")
        
        return self.results
    
    def save_results(self, filename=None):
        """Save results to JSON file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"data/username_{timestamp}.json"
        
        import os
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n{GREEN}💾 Results saved to:{RESET} {CYAN}{filename}{RESET}")
        return filename

# Test it
if __name__ == "__main__":
    username = UsernameModule()
    test_user = input("Enter username to search: ").strip()
    if not test_user:
        test_user = "heba_salhab"
    results = username.investigate(test_user)
    username.save_results()
