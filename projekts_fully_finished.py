import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

year = input("YYYY:")
month = input("MM:")
day = input("DD:")

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = f"https://www.nba.com/games?date={year}{month}{day}"
driver.get(url)
time.sleep(2)

# Check if there are any games on the specified day
komandas = driver.find_elements(By.CLASS_NAME, "MatchupCardTeamName_teamName__9YaBA")

if not komandas:
    print("Šajā dienā spēļu nav")
else:
    rezultati = []
    komandu_nosaukumi = []
    game_leaders_names = []
    text_links = []
    pts = []
    reb = []
    ast = []

    scores = driver.find_elements(By.CLASS_NAME, "MatchupCardScore_p__dfNvc.GameCardMatchup_matchupScoreCard__owb6w")
    for score in scores:
        text_content = score.text
        rezultati.append(text_content)

    komandas = driver.find_elements(By.CLASS_NAME, "MatchupCardTeamName_teamName__9YaBA")
    for komanda in komandas:
        nosaukums = komanda.text
        komandu_nosaukumi.append(nosaukums)

    gameleaders = driver.find_elements(By.CLASS_NAME, "GameCardLeaders_gclName__Oh5iE")
    for leader in gameleaders:
        vardsuzvards = leader.text
        game_leaders_names.append(vardsuzvards)

    stats = driver.find_elements(By.CLASS_NAME, "GameCardLeaders_gclRow__VMSee")
    for stat in stats:
        pts.append(stat.find_element(By.XPATH, './td[2]').text)
        reb.append(stat.find_element(By.XPATH, './td[3]').text)
        ast.append(stat.find_element(By.XPATH, './td[4]').text)

    links = driver.find_elements(By.CLASS_NAME, "Anchor_anchor__cSc3P.GameCardRecap_gcrLink__qvp_n")
    for link in links:
        href_value = link.get_attribute('href')
        text_links.append(href_value)
    print(text_links)
    print("-----------------------------------------------")
    print(f"Datums : {year}.{month}.{day}")
    Total_amount_of_games = int(len(komandu_nosaukumi) / 2)
    print(f"Spēļu skaits: {Total_amount_of_games}")
    
    for i in range(0, len(rezultati), 2):
        awayteam = komandu_nosaukumi[i]
        hometeam = komandu_nosaukumi[i + 1]
        awayscore = rezultati[i]
        homescore = rezultati[i + 1]
        best_away_player = game_leaders_names[i]
        best_home_player = game_leaders_names[i + 1]
        pointsforbestawayplayer = pts[i]
        pointsforbesthomeplayer = pts[i + 1]
        rebsforbestawayplayer = reb[i]
        rebsforbesthomeplayer = reb[i + 1]
        astforbestawayplayer = ast[i]
        astforbesthomeplayer = ast[i + 1]
        linking = text_links[i // 2]

        print(f"(Home){hometeam} - {awayteam}(Away)")
        print(f"{homescore} - {awayscore}")
        print(f"Labākais spēlētājs mājas komandā : {best_home_player}")
        print(f"Points : {pointsforbesthomeplayer} Rebounds : {rebsforbesthomeplayer} Assists : {astforbesthomeplayer}")
        if (int(pointsforbesthomeplayer) and int(rebsforbesthomeplayer) and int(astforbesthomeplayer)) >= 10:
            print(f"{best_home_player} ir ieguvis triple double")
        print(f"Labākais spēlētājs izbraukuma komandā : {best_away_player}")
        print(f"Points : {pointsforbestawayplayer} Rebounds : {rebsforbestawayplayer} Assists : {astforbestawayplayer}")
        if (int(pointsforbestawayplayer) and int(rebsforbestawayplayer) and int(astforbestawayplayer)) >= 10:
            print(f"{best_away_player} ir ieguvis triple double")
        print(f"Spēles labākie momenti : {linking}")
        print("-----------------------------------------------")

        
