#Copyright Adam. Don't be stealing my stuff man!

from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import csv
from filename_sanitizer import sanitize_path_fragment

links =[
"http://www.ufcstats.com/statistics/fighters?char=a&page=all",


]

csv_file = open('UFCDATA1.csv', 'w')
csv_writer = csv.writer(csv_file)                   #CSV code to open and setup excel file
csv_writer.writerow(['Name', 'Height (feet)', 'Weight (lbs)', 'Reach (inches)', 'Stance', 'SLpM', 'Str.Acc (%)', 'SApM', 'Str.Def', 'TD.Avg', 'TD.Acc', 'TD.Def', 'Sub.Avg']) 

for link in links:
    r = requests.get(link)  
    soup = BeautifulSoup(r.content, features="lxml")
    nameContainers = soup.find_all('table', {"class":'b-statistics__table'})

    for names in nameContainers:                    #For every article there is in the article div
        for name in names.find_all('tr', {"class":"b-statistics__table-row"}):   #For all the headers found
            for namelink in name.find_all('a', limit=1):
                if namelink.has_attr('href'):
                    #print(namelink['href'])
                    nameArray = [namelink['href']]
                    for link in nameArray:
                        r = requests.get(link)
                        soup = BeautifulSoup(r.content, features="lxml")
                        physicalStatsContainer = soup.find_all('ul', {"class":"b-list__box-list"})
                        name = soup.find('span', {"class":"b-content__title-highlight"})
                        #print(name.text.strip())
                        formattedFighterName = name.text.strip()
                        
                        physStatList = [_.get_text(strip=True) for _ in soup.find('ul', {'class': 'b-list__box-list'}).find_all('li')]
                        careerStatList = [_.get_text(strip=True) for _ in soup.find('div', {'class': 'b-list__info-box-left clearfix'}).find_all('li')]
                        #print(careerStatList)
                        csv_writer.writerow([formattedFighterName ,physStatList[0], physStatList[1], physStatList[2], physStatList[3], careerStatList[0], careerStatList[1],careerStatList[2],careerStatList[3],careerStatList[5],careerStatList[6],careerStatList[7], careerStatList[8]])

                        #for stat in physicalStatsContainer:
                            #print(stat.text)
                    
                            #x = stat.text.replace('Height:', '').replace('Reach:', '').replace('Weight:', '').replace('STANCE:', '').replace('SLpM:', '').replace('Str. Acc.:', '').replace('SApM:', '').replace('Str. Def:', '').replace('TD Avg.:', '').replace('TD Acc.:', '').replace('TD Def.:', '').replace('Sub. Avg.:', '') 
                            
                            #print(x)
                            

                        #careerStatsContainer = soup.find_all('ul', {"class":"b-list__box-list"})
                        #print(physicalStatsContainer)
                        

            #print(name.text)  #Print the header text for debugging




#region file 
#nextNode = header
            #while True:
                #nextNode = nextNode.nextSibling
                #if nextNode is None:
                    #break
                #if isinstance(nextNode, NavigableString):
                    #print (nextNode.strip())                        #This code essentially checks all the information between two headers
                #if isinstance(nextNode, Tag):
                    #if nextNode.name == "h2":
                        #break
                    #paragraph_text = nextNode.get_text(strip=True).strip()
                    # (paragraph_text)
            #print('\n')     #Blank line

            #     #Write the info to the excel file 
#endregion 
            


#csv_file.close()    #Close the csv after we done wid it