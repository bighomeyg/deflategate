from BeautifulSoup import BeautifulSoup
import commands

#Dictionary to relate state postal codes (in .svg map) to full name (in Twitter locations)
abbrevs = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming',
        'UP': 'Michigan'
}



svg_map = open('Blank_US_Map2.svg', 'r').read() 
soup = BeautifulSoup(svg_map)
tweet_freqs="state_histogramalphabetic.csv"

#Define style with blank variable for color
#From http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/
path_style = "font-size:12px;fill-rule:nonzero;stroke:#000000;" + \
             "stroke-width:1;stroke-linecap:butt;stroke-linejoin:bevel;" + \
             "stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;" + \
             "marker-start:none;fill:"
             
#Hex codes of red scale from http://colorbrewer2.org 
colors = ["#ADADAD", "#FEE5D9", "#FCBBA1", "#FC9272", "#FB6A4A", "#DE2D26", "#A50F15"]

paths=soup.findAll('path')

#Iterate through states (paths) on map, lookup histogram value, and assign color to path_style
for p in paths:
        try:
                current_state_code=p['id']
                full_state_name=abbrevs[current_state_code]
                tweetrate=commands.getoutput(''.join(\
                                "grep -m1 '" + full_state_name + "' state_histogramalphabetic.csv | awk -F',' '{print $2}'"))
                if tweetrate=='':
                        tweetrate=0       
                if int(tweetrate) > 125:
                        color_class = 6
                elif int(tweetrate) > 100:
                        color_class = 5
                elif int(tweetrate) > 75:
                        color_class = 4
                elif int(tweetrate) > 50:
                        color_class = 3
                elif int(tweetrate) > 25:
                        color_class = 2
                elif int(tweetrate) >= 1:
                        color_class = 1
                else:
                        color_class = 0
                
                color = colors[color_class]
                p['style'] = path_style + color
                print current_state_code, tweetrate, color
        
        except KeyError:
                continue
new_map=open("raw_data.svg", "w")        
new_map.write(soup.prettify())
new_map.close()