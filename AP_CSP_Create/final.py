from __future__ import print_function
import datetime
import time
import random


def title():
    """
    This function packages the data to hold titles that will randomly get generated in the code
    """
    title_1 =  """
         (()__(() 
         /       \ 
        ( /    \  \ 
         \ o o    / 
         (_()_)__/ \             
         / _,==.___ \ 
       (   |--|     ) 
       /\_.|__|'-.__/\_ 
      / (        /     \  
      \  \      (      / 
       )  '._____)    /  
      (((___.--(((___/
        Birth Date
    """
    title_2 = """
             __         __
            /  \.-\"\"\"-./  \  
            \    -   -    /
             |   o   o   |
             \  .-'''-.  /
              '-\__Y__/-'
                 `---`
              Birth Date
    """
    title_list = [title_1, title_2]
    title = random.choice(title_list) #randomly chooses a title
    print(title)
        
def birth_algorithm():
    """
    This functionn packages data that allows the user to use raw_inputs as well 
    as using a dictionary and many variable for the national holidays, and also 
    holds the major part of the code as well as using the datetime library
    """
    time.sleep(2)
    print("Please enter your birthday: ")
    JAN_1 = "National Hangover Day",
    JAN_2	 = "National Buffet Day",
    JAN_3	 = "JRR Tolkien Day"
    JAN_4	 = "National Spaghetti Day"
    JAN_5	 = "National Whipped Cream Day"
    JAN_6	 = "National Cuddle Up Day"
    JAN_7	 = "National Bobblehead Day"
    JAN_8	 = "National Bubble Bath Day"
    JAN_9	 = "National Law Enforcement Appreciation Day"
    JAN_10	 = "National Houseplant Appreciation Day"
    JAN_11	 = "National Milk Day"
    JAN_12	 = "National Youth Day"
    JAN_13	 = "National Rubber Ducky Day"
    JAN_14	 = "National Dress Up Your Pet Day"
    JAN_15	 = "National Bagel Day"
    JAN_16	 = "National Fig Newton Day"
    JAN_17	 = "National Hot Buttered Rum Day"
    JAN_18	 = "National Winnie the Pooh Day"
    JAN_19	 = "National Popcorn Day"
    JAN_20	 = "National Cheese Lover's Day"
    JAN_21	 = "Museum Selfie Day"
    JAN_22	 = "National Blonde Brownie Day"
    JAN_23	 = "National Pie Day"
    JAN_24	 = "National Peanut Butter Day"
    JAN_25	 = "National Opposite Day"
    JAN_26	 = "National Spouses Day"
    JAN_27	 = "National Chocolate Cake Day"
    JAN_28	 = "National Bubble Wrap Appreciation Day"
    JAN_29	 = "National Puzzle Day"
    JAN_30	 = "National Croissant Day"
    JAN_31	 = "National Hot Chocolate Day"
    FEB_1	 = "National Bubble Gum Day	"
    FEB_2	 = "Candlemas Day"
    FEB_3	 = "National Carrot Cake Day"
    FEB_4	 = "National Eat Ice Cream for Breakfast Day"
    FEB_5	 = "National Chocolate Fondue Day"
    FEB_6	 = "National Frozen Yogurt Day"
    FEB_7	 = "National Fettuccine Alfredo Day"
    FEB_8	 = "National Boy Scout Day"
    FEB_9	 = "National Pizza Day"
    FEB_10	 = "National Umbrella Day"
    FEB_11	 = "National Inventors' Day"
    FEB_12	 = "National Clean Out Your Computer Day"
    FEB_13	 = "National Tortellini Day"
    FEB_14	 = "National Donor Day"
    FEB_15	 = "Singles Awareness Day"
    FEB_16	 = "National Almond Day"
    FEB_17	 = "Random Act of Kindness Day"
    FEB_18	 = "National Drink Wine Day"
    FEB_19	 = "Tug of War Day"
    FEB_20	 = "National Love Your Pet Day"
    FEB_21	 = "National Sticky Bun Day"
    FEB_22	 = "National Margarita Day"
    FEB_23	 = "International Dog Biscuit Appreciation Day"
    FEB_24	 = "National Tortilla Chip Day"
    FEB_25	 = "National Clam Chowder Day"
    FEB_26	 = "National Pistachio Day"
    FEB_27	 = "National Pokemon Day"
    FEB_28	 = "National Chili Day"
    MAR_1	  = "National Day of Unplugging	 "
    MAR_2	  = "National Read Across America Day	 "
    MAR_3	  = "National If Pets Had Thumbs Day	 "
    MAR_4	  = "National Grammar Day	 "
    MAR_5	  = "National Absinthe Day	 "
    MAR_6	  = "National Oreo Cookie Day	 "
    MAR_7	  = "National Cereal Day	 "
    MAR_8	  = "International Women's Day	 "
    MAR_9	  = "National Meatball Day	 "
    MAR_10	  = "National Landline Telephone Day	 "
    MAR_11	  = "National Napping Day	 "
    MAR_12	  = "National Pancake Day	 "
    MAR_13	  = "National K9 Veterans Day	 "
    MAR_14	  = "National Pi Day	 "
    MAR_15	  = "Red Nose Day	 "
    MAR_16	  = "National Corn Dog Day	 "
    MAR_17	  = "St. Patrick's Day	 "
    MAR_18	  = "Awkward Moments Day	 "
    MAR_19	  = "National Poultry Day	 "
    MAR_20	  = "National Ravioli Day	 "
    MAR_21	  = "World Poetry Day	 "
    MAR_22	  = "National Goof Off Day	 "
    MAR_23	  = "World Meteorological Day	 "
    MAR_24	  = "National Cheesesteak Day	 "
    MAR_25	  = "International Waffle Day	 "
    MAR_26	  = "National Spinach Day	 "
    MAR_27	  = "Quentin Tarantino's Birthday	 "
    MAR_28	  = "Respect Your Cat Day	 "
    MAR_29	  = "National Mom and Pop Business Owners Day	 "
    MAR_30	  = "National Doctors' Day	 "
    MAR_31	  = "World Backup Day	 "
    APR_1	  = "April Fools' Day	  "
    APR_2	  = "National Peanut Butter and Jelly Day	  "
    APR_3	  = "World Party Day	  "
    APR_4	  = "National Burrito Day	  "
    APR_5	  = "National Deep Dish Pizza Day	  "
    APR_6	  = "New Beer's Eve	  "
    APR_7	  = "World Health Day	  "
    APR_8	  = "National Empanada Day	  "
    APR_9	  = "National Winston Churchill Day	  "
    APR_10	  = "National Siblings Day	  "
    APR_11	  = "National Pet Day	  "
    APR_12	  = "National Day of Silence	  "
    APR_13	  = "National Make Lunch Count Day	  "
    APR_14	  = "National Ex Spouse Day	  "
    APR_15	  = "National Laundry Day	  "
    APR_16	  = "Wear Pajamas to Work Day	  "
    APR_17	  = "National Cheeseball Day	  "
    APR_18	  = "National High Five Day	  "
    APR_19	  = "National Garlic Day	  "
    APR_20	  = "National Look-Alike Day	  "
    APR_21	  = "National Kindergarten Day	  "
    APR_22	  = "National Jelly Bean Day	  "
    APR_23	  = "National Picnic Day	  "
    APR_24	  = "National Pigs in a Blanket Day	  "
    APR_25	  = "ANZAC Day	  "
    APR_26	  = "National Pretzel Day	  "
    APR_27	  = "National Drug Take Back Day	  "
    APR_28	  = "National Superhero Day	  "
    APR_29	  = "International Dance Day	  "
    APR_30	  = "International Jazz Day	  "
    MAY_1	  =  "May Day	  "
    MAY_2	  =  "National Brothers and Sisters Day	  "
    MAY_3	  =  "National Paranormal Day	  "
    MAY_4	  =  "Star Wars Day	  "
    MAY_5	  =  "National Hoagie Day	  "
    MAY_6	  =  "National Tourist Appreciation Day	  "
    MAY_7	  =  "National Tourism Day	  "
    MAY_8	  =  "National Have a Coke Day	  "
    MAY_9	  =  "National Moscato Day	  "
    MAY_10	  =  "National Clean Your Room Day	  "
    MAY_11	  =  "World Migratory Bird Day	  "
    MAY_12	  =  "Mother's Day	  "
    MAY_13	  =  "National Fruit Cocktail Day	  "
    MAY_14	  =  "National Buttermilk Biscuit Day	  "
    MAY_15	  =  "International Day of Families	  "
    MAY_16	  =  "National Mimosa Day	  "
    MAY_17	  =  "National Pizza Party Day	  "			
    MAY_18	  =  "National Armed Forces Day	  "			
    MAY_19	  =  "National Endangered Species Day	  "			
    MAY_20	  =  "National Be a Millionaire Day	  "
    MAY_21	  =  "National Waiters and Waitresses Day"		
    MAY_22	  =  "National Maritime Day	  "
    MAY_23	  =  "National Taffy Day	  "
    MAY_24	  =  "National Brother's Day	  "		
    MAY_25	  =  "National Wine Day	  "
    MAY_26	  =  "National Paper Airplane Day	  "
    MAY_27	  =  "Memorial Day	  "
    MAY_28	  =  "National Brisket Day	  "			
    MAY_29	  =  "Learn About Composting Day	  "
    MAY_30	  =  "National Mint Julep Day	  "
    MAY_31	  =  "World No Tobacco Day	  "
    JUN_1	  =  "National Olive Day	"
    JUN_2     =  "no holidays         "
    JUN_3	  =  "World Bicycle Day	"
    JUN_4	  =  "National Day of Civic Hacking	"
    JUN_5	  =  "World Environment Day	"
    JUN_6	  =  "National Yo-Yo Day	"
    JUN_7	  =  "Global Running Day	"
    JUN_8	  =  "World Oceans Day	"
    JUN_9	  =  "National Donald Duck Day	"
    JUN_10	  =  "National Iced Tea Day	"
    JUN_11	  =  "National Corn on the Cob Day	"
    JUN_12	  =  "National Loving Day	"
    JUN_13	  =  "National Sewing Machine Day	"
    JUN_14	  =  "World Blood Donor Day	"
    JUN_15	  =  "World Elder Abuse Awareness Day	"
    JUN_16	  =  "National Fudge Day	"
    JUN_17	  =  "National Take Your Cat to Work Day	"
    JUN_18	  =  "National Go Fishing Day	"
    JUN_19	  =  "National Garfield the Cat Day	"			
    JUN_20	  =  "National American Eagle Day	"	
    JUN_21	  =  "National Selfie Day	"
    JUN_22	  =  "National Onion Ring Day	"
    JUN_23	  =  "National Hydration Day	"
    JUN_24	  =  "Saint-Jean-Baptiste Day	"
    JUN_25	  =  "International Day of the Seafarer	"
    JUN_26	  =  "National Chocolate Pudding Day	"
    JUN_27	  =  "National Sunglasses Day	"		
    JUN_28	  =  "National Tapioca Day	"
    JUN_29	  =  "Hug Holiday	"
    JUN_30	  =  "International Asteroid Day	"
    JUL_1	 = "International Joke Day	"	
    JUL_2	 = "World UFO Day	"	
    JUL_3	 = "National Stay Out of the Sun Day	"	
    JUL_4	 = "Independence Day	"	
    JUL_5	 = "National Bikini Day	"	
    JUL_6	 = "National Fried Chicken Day	"	
    JUL_7	 = "First Day of NAIDOC Week	"	
    JUL_8	 = "National Video Game Day	"	
    JUL_9	 = "National Sugar Cookie Day	"	
    JUL_10	 = "National Kitten Day	"	
    JUL_11	 = "World Population Day	"	
    JUL_12	 = "Orangemen's Day	"	
    JUL_13	 = "National French Fry Day	"	
    JUL_14	 = "Bastille Day	"	
    JUL_15	 = "National Give Something Away Day	"	
    JUL_16	 = "National Corn Fritter Day	"	
    JUL_17	 = "National Hot Dog Day	"	
    JUL_18	 = "National Caviar Day	"	
    JUL_19	 = "National Daiquiri Day	"	
    JUL_20	 = "National Moon Day	"	
    JUL_21	 = "National Ice Cream Day	"	
    JUL_22	 = "National Hammock Day	"	
    JUL_23	 = "National Gorgeous Grandma Day	"	
    JUL_24	 = "National Cousins Day	"	
    JUL_25	 = "National Wine and Cheese Day	"	
    JUL_26	 = "National Aunt and Uncle Day	"	
    JUL_27	 = "National Scotch Day	"	
    JUL_28	 = "World Hepatitis Day	"	
    JUL_29	 = "National Lasagna Day	"	
    JUL_30	 = "National Father-in-Law Day	"	
    JUL_31	 = "Harry Potter's Birthday	"	
    AUG_1	 = "Spider-Man Day	"			
    AUG_2	 = "National Ice Cream Sandwich Day	"
    AUG_3	 = "National Mustard Day	"
    AUG_4	 = "National Sisters Day	"				
    AUG_5	 = "British Columbia Day	"
    AUG_6    = "no holiday              "
    AUG_7	 = "National Lighthouse Day	"				
    AUG_8	 = "Peace Festival in Augsburg	"				
    AUG_9	 = "National Women's Day	"
    AUG_10	 = "National Lazy Day	"
    AUG_11	 = "National Son and Daughter Day	"
    AUG_12	 = "International Youth Day	"
    AUG_13	 = "International Lefthanders Day	"
    AUG_14	 = "National Financial Awareness Day	"
    AUG_15	 = "Chant at the Moon Day	"
    AUG_16	 = "National Tell A Joke Day	"
    AUG_17	 = "National Black Cat Appreciation Day	"
    AUG_18	 = "National Fajita Day	"
    AUG_19	 = "National Potato Day	"				
    AUG_20	 = "National Lemonade Day	"			
    AUG_21	 = "National Senior Citizens Day	"				
    AUG_22	 = "National Take Your Cat to the Vet Day	"																
    AUG_23	 = "National Sponge Cake Day	"
    AUG_24	 = "National Waffle Day	"
    AUG_25	 = "National Banana Split Day	"				
    AUG_26	 = "National Dog Day	"				
    AUG_27	 = "National Just Because Day	"
    AUG_28	 = "National Red Wine Day	"
    AUG_29	 = "National Lemon Juice Day	"
    AUG_30	 = "the Islamic New Year	"
    AUG_31	 = "National Trail Mix Day	"
    SEPT_1	 = "College Colors Day	"
    SEPT_2	 = "World Coconut Day	"
    SEPT_3	 = "National Skyscraper Day	"
    SEPT_4	 = "National Wildlife Day	"
    SEPT_5	 = "National Cheese Pizza Day	"
    SEPT_6	 = "National Read a Book Day	"
    SEPT_7	 = "National Beer Lover's Day	"
    SEPT_8	 = "Day of the Homeland	"		
    SEPT_9	 = "National Wiener Schnitzel Day	"
    SEPT_10	 = "World Suicide Prevention Day	"
    SEPT_11	 = "National Make Your Bed Day	"
    SEPT_12	 = "National Video Games Day	"
    SEPT_13	 = "European Heritage Days	"
    SEPT_14	 = "German Language Day	"
    SEPT_15	 = "Batman Day	"
    SEPT_16	 = "National Guacamole Day	"
    SEPT_17	 = "Constitution Day	"
    SEPT_18	 = "National Cheeseburger Day	"
    SEPT_19	 = "International Talk Like a Pirate Day	"
    SEPT_20	 = "National Queso Day	"
    SEPT_21	 = "International Day of Peace	"
    SEPT_22	 = "the Falls Prevention Awareness Day	"
    SEPT_23	 = "First Day of Fall	"
    SEPT_24	 = "National Cherries Jubilee Day	"
    SEPT_25	 = "Heritage Day	"
    SEPT_26	 = "National Pancake Day	"
    SEPT_27	 = "World Tourism Day	"
    SEPT_28	 = "National Bunny Day	"
    SEPT_29	 = "Family Health & Fitness Day USA	"
    SEPT_30	 = "National Love People Day	"
    OCT_1	 = "World Vegetarian Day	"
    OCT_2	 = "International Day of Non-Violence	"
    OCT_3	 = "National Poetry Day	"
    OCT_4	 = "National Cinnamon Roll Day	"
    OCT_5	 = "World Teachers Day	"
    OCT_6	 = "National Transfer Money to Your Daughter Day	"
    OCT_7	 = "National Child Health Day	"
    OCT_8	 = "National Fluffernutter Day	"
    OCT_9	 = "World Post Day	"
    OCT_10	 = "National Cake Decorating Day	"
    OCT_11	 = "World Obesity Day	"
    OCT_12	 = "National Coaches Day	"
    OCT_13	 = "World Hospice and Palliative Care Day	"
    OCT_14	 = "Columbus Day	"
    OCT_15	 = "World Maths Day	"
    OCT_16	 = "National Liqueur Day	"
    OCT_17	 = "National Clean Your Virtual Desktop Day	"
    OCT_18	 = "National Chocolate Cupcake Day	"
    OCT_19	 = "World Pediatric Bone and Joint Day	"
    OCT_20	 = "International Sloth Day	"
    OCT_21	 = "National Reptile Day	"
    OCT_22	 = "National Nut Day	"
    OCT_23	 = "National Boston Cream Pie Day	"
    OCT_24	 = "National Bologna Day	"
    OCT_25	 = "National I Care About You Day	"
    OCT_26	 = "National Pumpkin Day	"
    OCT_27	 = "National Mentoring Day	"
    OCT_28	 = "National First Responders Day	"
    OCT_29	 = "National Cat Day	"
    OCT_30	 = "National Text Your Ex Day	"
    OCT_31	 = "National Caramel Apple Day	"
    NOV_1	 = "National Vinegar Day	 "
    NOV_2	 = "Day of the Dead	 "
    NOV_3	 = "National Sandwich Day	 "
    NOV_4	 = "Job Action Day	 "
    NOV_5	 = "American Football Day	 "
    NOV_6	 = "National Nachos Day	 "
    NOV_7	 = "International Stout Day	 "
    NOV_8	 = "S.T.E.M. - S.T.E.A.M. Day	 "
    NOV_9	 = "Go to an Art Museum Day	 "
    NOV_10	 = "International Accounting Day	 "
    NOV_11	 = "Veterans Day	 "
    NOV_12	 = "National Happy Hour Day	 "
    NOV_13	 = "World Kindness Day	 "
    NOV_14	 = "National Pickle Day	 "
    NOV_15	 = "National Recycling Day	 "
    NOV_16	 = "International Day For Tolerance	 "
    NOV_17	 = "National Unfriend Day	 "
    NOV_18	 = "Mickey Mouse Day	 "
    NOV_19	 = "World Toilet Day	 "
    NOV_20	 = "Future Teachers of America Day	 "
    NOV_21	 = "World Television Day	 "
    NOV_22	 = "Go For A Ride Day	 "
    NOV_23	 = "International Survivors of Suicide Day	 "
    NOV_24	 = "no holiday	 "
    NOV_25	 = "International Day for the Elimination of Violence Against Women	 "
    NOV_26	 = "National Cake Day	 "
    NOV_27	 = "no holiday	 "
    NOV_28	 = "National Day of Mourning	 "
    NOV_29	 = "Black Friday	 "
    NOV_30	 = "Small Business Saturday	 "
    DEC_1	  = "World AIDS Day	 "
    DEC_2	  = "National Mutt Day	 "
    DEC_3	  = "Giving Tuesday	 "
    DEC_4	  = "National Cookie Day	 "
    DEC_5	  = "International Ninja Day	 "
    DEC_6	  = "National Miners Day	 "
    DEC_7	  = "International Civil Aviation Day	 "
    DEC_8	  = "National Bartender Day	 "
    DEC_9	  = "National Pastry Day	 "
    DEC_10	  = "National Lager Day	 "
    DEC_11	  = "International Mountain Day	 "
    DEC_12	  = "National Ding-A-Ling Day	 "
    DEC_13	  = "U.S. National Guard Birthday	 "
    DEC_14	  = "National Bouillabaisse Day	 "
    DEC_15	  = "National Cupcake Day	 "
    DEC_16	  = "National Chocolate Covered Anything Day	 "
    DEC_17	  = "ational Maple Syrup Day	 "
    DEC_18	  = "Arabic Language Day	 "
    DEC_19	  = "National Emo Day	 "
    DEC_20	  = "National Ugly Sweater Day	 "
    DEC_21	  = "National Coquito Day	 "
    DEC_22	  = "National Cookie Exchange Day	 "
    DEC_23	  = "Festivus	 "
    DEC_24	  = "Christmas Eve	 "
    DEC_25	  = "Christmas	 "
    DEC_26	  = "National Thank You Note Day	 "
    DEC_27	  = "National Fruitcake Day	 "
    DEC_28	  = "National Download Day	 "
    DEC_29	  = "Still Need To Do Day	 "
    DEC_30	  = "National Bacon Day	 "
    DEC_31	  = "Hogmanay	 "
    
    currentDT = datetime.datetime.now()
    
    year = raw_input("Year of birth: ")
    month = raw_input("Month of birth: ")
    day = raw_input("Day of birth: ")
    holiday = {
        
        JAN_1 : "1/1/%s" %(year),
        JAN_2 : "1/2/%s" %(year),
        JAN_3 : "1/3/%s" %(year),
        JAN_4 : "1/4/%s" %(year),
        JAN_5 : "1/5/%s" %(year),
        JAN_6 : "1/6/%s" %(year),
        JAN_7 : "1/7/%s" %(year),
        JAN_8 : "1/8/%s" %(year),
        JAN_9 : "1/9/%s" %(year),
        JAN_10: "1/10/%s" %(year),
        JAN_11: "1/11/%s" %(year),
        JAN_12: "1/12/%s" %(year),
        JAN_13: "1/13/%s" %(year),
        JAN_14: "1/14/%s" %(year),
        JAN_15: "1/15/%s" %(year),
        JAN_16: "1/16/%s" %(year),
        JAN_17: "1/17/%s" %(year),
        JAN_18: "1/18/%s" %(year),
        JAN_19: "1/29/%s" %(year),
        JAN_20: "1/20/%s" %(year),
        JAN_21: "1/21/%s" %(year),
        JAN_22: "1/22/%s" %(year),
        JAN_23: "1/23/%s" %(year),
        JAN_24: "1/24/%s" %(year),
        JAN_25: "1/25/%s" %(year),
        JAN_26: "1/26/%s" %(year),
        JAN_27: "1/27/%s" %(year),
        JAN_28: "1/28/%s" %(year),
        JAN_29: "1/29/%s" %(year),
        JAN_30: "1/30/%s" %(year),
        JAN_31: "1/31/%s" %(year),
        FEB_1 : "2/1/%s" %(year),
        FEB_2 : "2/2/%s" %(year),
        FEB_3 : "2/3/%s" %(year),
        FEB_4 : "2/4/%s" %(year),
        FEB_5 : "2/5/%s" %(year),
        FEB_6 : "2/6/%s" %(year),
        FEB_7 : "2/7/%s" %(year),
        FEB_8 : "2/8/%s" %(year),
        FEB_9 : "2/9/%s" %(year),
        FEB_10: "2/10/%s" %(year),
        FEB_11: "2/11/%s" %(year),
        FEB_12: "2/12/%s" %(year),
        FEB_13: "2/13/%s" %(year),
        FEB_14: "2/14/%s" %(year),
        FEB_15: "2/15/%s" %(year),
        FEB_16: "2/16/%s" %(year),
        FEB_17: "2/17/%s" %(year),
        FEB_18: "2/18/%s" %(year),
        FEB_19: "2/19/%s" %(year),
        FEB_20: "2/20/%s" %(year),
        FEB_21: "2/21/%s" %(year),
        FEB_22: "2/22/%s" %(year),
        FEB_23: "2/23/%s" %(year),
        FEB_24: "2/24/%s" %(year),
        FEB_25: "2/25/%s" %(year),
        FEB_26: "2/26/%s" %(year),
        FEB_27: "2/27/%s" %(year),
        FEB_28: "2/28/%s" %(year),
        MAR_1 :"3/1/%s" %(year),
        MAR_2 :"3/2/%s" %(year),
        MAR_3 :"3/3/%s" %(year),
        MAR_4 :"3/4/%s" %(year),
        MAR_5 :"3/5/%s" %(year),
        MAR_6 :"3/6/%s" %(year),
        MAR_7 :"3/7/%s" %(year),
        MAR_8 :"3/8/%s" %(year),
        MAR_9 :"3/9/%s" %(year),
        MAR_10:"3/10/%s" %(year),
        MAR_11:"3/11/%s" %(year),
        MAR_12:"3/12/%s" %(year),
        MAR_13:"3/13/%s" %(year),
        MAR_14:"3/14/%s" %(year),
        MAR_15:"3/15/%s" %(year),
        MAR_16:"3/16/%s" %(year),
        MAR_17:"3/17/%s" %(year),
        MAR_18:"3/18/%s" %(year),
        MAR_19:"3/29/%s" %(year),
        MAR_20:"3/20/%s" %(year),
        MAR_21:"3/21/%s" %(year),
        MAR_22:"3/22/%s" %(year),
        MAR_23:"3/23/%s" %(year),
        MAR_24:"3/24/%s" %(year),
        MAR_25:"3/25/%s" %(year),
        MAR_26:"3/26/%s" %(year),
        MAR_27:"3/27/%s" %(year),
        MAR_28:"3/28/%s" %(year),
        MAR_29:"3/29/%s" %(year),
        MAR_30:"3/30/%s" %(year),
        MAR_31:"3/31/%s" %(year),
        APR_1 : "4/1/%s" %(year),
        APR_2 : "4/2/%s" %(year),
        APR_3 : "4/3/%s" %(year),
        APR_4 : "4/4/%s" %(year),
        APR_5 : "4/5/%s" %(year),
        APR_6 : "4/6/%s" %(year),
        APR_7 : "4/7/%s" %(year),
        APR_8 : "4/8/%s" %(year),
        APR_9 : "4/9/%s" %(year),
        APR_10: "4/10/%s" %(year),
        APR_11: "4/11/%s" %(year),
        APR_12: "4/12/%s" %(year),
        APR_13: "4/13/%s" %(year),
        APR_14: "4/14/%s" %(year),
        APR_15: "4/15/%s" %(year),
        APR_16: "4/16/%s" %(year),
        APR_17: "4/17/%s" %(year),
        APR_18: "4/18/%s" %(year),
        APR_19: "4/29/%s" %(year),
        APR_20: "4/20/%s" %(year),
        APR_21: "4/21/%s" %(year),
        APR_22: "4/22/%s" %(year),
        APR_23: "4/23/%s" %(year),
        APR_24: "4/24/%s" %(year),
        APR_25: "4/25/%s" %(year),
        APR_26: "4/26/%s" %(year),
        APR_27: "4/27/%s" %(year),
        APR_28: "4/28/%s" %(year),
        APR_29: "4/29/%s" %(year),
        APR_30: "4/30/%s" %(year),
        MAY_1 : "5/1/%s" %(year),
        MAY_2 : "5/2/%s" %(year),
        MAY_3 : "5/3/%s" %(year),
        MAY_4 : "5/4/%s" %(year),
        MAY_5 : "5/5/%s" %(year),
        MAY_6 : "5/6/%s" %(year),
        MAY_7 : "5/7/%s" %(year),
        MAY_8 : "5/8/%s" %(year),
        MAY_9 : "5/9/%s" %(year),
        MAY_10: "5/10/%s" %(year),
        MAY_11: "5/11/%s" %(year),
        MAY_12: "5/12/%s" %(year),
        MAY_13: "5/13/%s" %(year),
        MAY_14: "5/14/%s" %(year),
        MAY_15: "5/15/%s" %(year),
        MAY_16: "5/16/%s" %(year),
        MAY_17: "5/17/%s" %(year),
        MAY_18: "5/18/%s" %(year),
        MAY_19: "5/29/%s" %(year),
        MAY_20: "5/20/%s" %(year),
        MAY_21: "5/21/%s" %(year),
        MAY_22: "5/22/%s" %(year),
        MAY_23: "5/23/%s" %(year),
        MAY_24: "5/24/%s" %(year),
        MAY_25: "5/25/%s" %(year),
        MAY_26: "5/26/%s" %(year),
        MAY_27: "5/27/%s" %(year),
        MAY_28: "5/28/%s" %(year),
        MAY_29: "5/29/%s" %(year),
        MAY_30: "5/30/%s" %(year),
        MAY_31: "5/31/%s" %(year),
        JUN_1 : "6/1/%s" %(year),
        JUN_2 : "6/2/%s" %(year),
        JUN_3 : "6/3/%s" %(year),
        JUN_4 : "6/4/%s" %(year),
        JUN_5 : "6/5/%s" %(year),
        JUN_6 : "6/6/%s" %(year),
        JUN_7 : "6/7/%s" %(year),
        JUN_8 : "6/8/%s" %(year),
        JUN_9 : "6/9/%s" %(year),
        JUN_10: "6/10/%s" %(year),
        JUN_11: "6/11/%s" %(year),
        JUN_12: "6/12/%s" %(year),
        JUN_13: "6/13/%s" %(year),
        JUN_14: "6/14/%s" %(year),
        JUN_15: "6/15/%s" %(year),
        JUN_16: "6/16/%s" %(year),
        JUN_17: "6/17/%s" %(year),
        JUN_18: "6/18/%s" %(year),
        JUN_19: "6/29/%s" %(year),
        JUN_20: "6/20/%s" %(year),
        JUN_21: "6/21/%s" %(year),
        JUN_22: "6/22/%s" %(year),
        JUN_23: "6/23/%s" %(year),
        JUN_24: "6/24/%s" %(year),
        JUN_25: "6/25/%s" %(year),
        JUN_26: "6/26/%s" %(year),
        JUN_27: "6/27/%s" %(year),
        JUN_28: "6/28/%s" %(year),
        JUN_29: "6/29/%s" %(year),
        JUN_30: "6/30/%s" %(year),
        JUL_1 : "5/1/%s" %(year),
        JUL_2 : "5/2/%s" %(year),
        JUL_3 : "5/3/%s" %(year),
        JUL_4 : "5/4/%s" %(year),
        JUL_5 : "5/5/%s" %(year),
        JUL_6 : "5/6/%s" %(year),
        JUL_7 : "5/7/%s" %(year),
        JUL_8 : "5/8/%s" %(year),
        JUL_9 : "5/9/%s" %(year),
        JUL_10: "5/10/%s" %(year),
        JUL_11: "5/11/%s" %(year),
        JUL_12: "5/12/%s" %(year),
        JUL_13: "5/13/%s" %(year),
        JUL_14: "5/14/%s" %(year),
        JUL_15: "5/15/%s" %(year),
        JUL_16: "5/16/%s" %(year),
        JUL_17: "5/17/%s" %(year),
        JUL_18: "5/18/%s" %(year),
        JUL_19: "5/29/%s" %(year),
        JUL_20: "5/20/%s" %(year),
        JUL_21: "5/21/%s" %(year),
        JUL_22: "5/22/%s" %(year),
        JUL_23: "5/23/%s" %(year),
        JUL_24: "5/24/%s" %(year),
        JUL_25: "5/25/%s" %(year),
        JUL_26: "5/26/%s" %(year),
        JUL_27: "5/27/%s" %(year),
        JUL_28: "5/28/%s" %(year),
        JUL_29: "5/29/%s" %(year),
        JUL_30: "5/30/%s" %(year),
        JUL_31: "5/31/%s" %(year),
        AUG_1 : "8/1/%s" %(year),
        AUG_2 : "8/2/%s" %(year),
        AUG_3 : "8/3/%s" %(year),
        AUG_4 : "8/4/%s" %(year),
        AUG_5 : "8/5/%s" %(year),
        AUG_6 : "8/6/%s" %(year),
        AUG_7 : "8/7/%s" %(year),
        AUG_8 : "8/8/%s" %(year),
        AUG_9 : "8/9/%s" %(year),
        AUG_10: "8/10/%s" %(year),
        AUG_11: "8/11/%s" %(year),
        AUG_12: "8/12/%s" %(year),
        AUG_13: "8/13/%s" %(year),
        AUG_14: "8/14/%s" %(year),
        AUG_15: "8/15/%s" %(year),
        AUG_16: "8/16/%s" %(year),
        AUG_17: "8/17/%s" %(year),
        AUG_18: "8/18/%s" %(year),
        AUG_19: "8/29/%s" %(year),
        AUG_20: "8/20/%s" %(year),
        AUG_21: "8/21/%s" %(year),
        AUG_22: "8/22/%s" %(year),
        AUG_23: "8/23/%s" %(year),
        AUG_24: "8/24/%s" %(year),
        AUG_25: "8/25/%s" %(year),
        AUG_26: "8/26/%s" %(year),
        AUG_27: "8/27/%s" %(year),
        AUG_28: "8/28/%s" %(year),
        AUG_29: "8/29/%s" %(year),
        AUG_30: "8/30/%s" %(year),
        AUG_31: "8/31/%s" %(year),
        SEPT_1 : "9/1/%s" %(year),
        SEPT_2 : "9/2/%s" %(year),
        SEPT_3 : "9/3/%s" %(year),
        SEPT_4 : "9/4/%s" %(year),
        SEPT_5 : "9/5/%s" %(year),
        SEPT_6 : "9/6/%s" %(year),
        SEPT_7 : "9/7/%s" %(year),
        SEPT_8 : "9/8/%s" %(year),
        SEPT_9 : "9/9/%s" %(year),
        SEPT_10: "9/10/%s" %(year),
        SEPT_11: "9/11/%s" %(year),
        SEPT_12: "9/12/%s" %(year),
        SEPT_13: "9/13/%s" %(year),
        SEPT_14: "9/14/%s" %(year),
        SEPT_15: "9/15/%s" %(year),
        SEPT_16: "9/16/%s" %(year),
        SEPT_17: "9/17/%s" %(year),
        SEPT_18: "9/18/%s" %(year),
        SEPT_19: "9/29/%s" %(year),
        SEPT_20: "9/20/%s" %(year),
        SEPT_21: "9/21/%s" %(year),
        SEPT_22: "9/22/%s" %(year),
        SEPT_23: "9/23/%s" %(year),
        SEPT_24: "9/24/%s" %(year),
        SEPT_25: "9/25/%s" %(year),
        SEPT_26: "9/26/%s" %(year),
        SEPT_27: "9/27/%s" %(year),
        SEPT_28: "9/28/%s" %(year),
        SEPT_29: "9/29/%s" %(year),
        SEPT_30: "9/30/%s" %(year),
        OCT_1 : "10/1/%s" %(year),
        OCT_2 : "10/2/%s" %(year),
        OCT_3 : "10/3/%s" %(year),
        OCT_4 : "10/4/%s" %(year),
        OCT_5 : "10/5/%s" %(year),
        OCT_6 : "10/6/%s" %(year),
        OCT_7 : "10/7/%s" %(year),
        OCT_8 : "10/8/%s" %(year),
        OCT_9 : "10/9/%s" %(year),
        OCT_10: "10/10/%s" %(year),
        OCT_11: "10/11/%s" %(year),
        OCT_12: "10/12/%s" %(year),
        OCT_13: "10/13/%s" %(year),
        OCT_14: "10/14/%s" %(year),
        OCT_15: "10/15/%s" %(year),
        OCT_16: "10/16/%s" %(year),
        OCT_17: "10/17/%s" %(year),
        OCT_18: "10/18/%s" %(year),
        OCT_19: "10/29/%s" %(year),
        OCT_20: "10/20/%s" %(year),
        OCT_21: "10/21/%s" %(year),
        OCT_22: "10/22/%s" %(year),
        OCT_23: "10/23/%s" %(year),
        OCT_24: "10/24/%s" %(year),
        OCT_25: "10/25/%s" %(year),
        OCT_26: "10/26/%s" %(year),
        OCT_27: "10/27/%s" %(year),
        OCT_28: "10/28/%s" %(year),
        OCT_29: "10/29/%s" %(year),
        OCT_30: "10/30/%s" %(year),
        OCT_31: "10/31/%s" %(year),
        NOV_1 : "11/1/%s" %(year),
        NOV_2 : "11/2/%s" %(year),
        NOV_3 : "11/3/%s" %(year),
        NOV_4 : "11/4/%s" %(year),
        NOV_5 : "11/5/%s" %(year),
        NOV_6 : "11/6/%s" %(year),
        NOV_7 : "11/7/%s" %(year),
        NOV_8 : "11/8/%s" %(year),
        NOV_9 : "11/9/%s" %(year),
        NOV_10: "11/10/%s" %(year),
        NOV_11: "11/11/%s" %(year),
        NOV_12: "11/12/%s" %(year),
        NOV_13: "11/13/%s" %(year),
        NOV_14: "11/14/%s" %(year),
        NOV_15: "11/15/%s" %(year),
        NOV_16: "11/16/%s" %(year),
        NOV_17: "11/17/%s" %(year),
        NOV_18: "11/18/%s" %(year),
        NOV_19: "11/29/%s" %(year),
        NOV_20: "11/20/%s" %(year),
        NOV_21: "11/21/%s" %(year),
        NOV_22: "11/22/%s" %(year),
        NOV_23: "11/23/%s" %(year),
        NOV_24: "11/24/%s" %(year),
        NOV_25: "11/25/%s" %(year),
        NOV_26: "11/26/%s" %(year),
        NOV_27: "11/27/%s" %(year),
        NOV_28: "11/28/%s" %(year),
        NOV_29: "11/29/%s" %(year),
        NOV_30: "11/30/%s" %(year),
        DEC_1 : "12/1/%s" %(year),
        DEC_2 : "12/2/%s" %(year),
        DEC_3 : "12/3/%s" %(year),
        DEC_4 : "12/4/%s" %(year),
        DEC_5 : "12/5/%s" %(year),
        DEC_6 : "12/6/%s" %(year),
        DEC_7 : "12/7/%s" %(year),
        DEC_8 : "12/8/%s" %(year),
        DEC_9 : "12/9/%s" %(year),
        DEC_10: "12/10/%s" %(year),
        DEC_11: "12/11/%s" %(year),
        DEC_12: "12/12/%s" %(year),
        DEC_13: "12/13/%s" %(year),
        DEC_14: "12/14/%s" %(year),
        DEC_15: "12/15/%s" %(year),
        DEC_16: "12/16/%s" %(year),
        DEC_17: "12/17/%s" %(year),
        DEC_18: "12/18/%s" %(year),
        DEC_19: "12/29/%s" %(year),
        DEC_20: "12/20/%s" %(year),
        DEC_21: "12/21/%s" %(year),
        DEC_22: "12/22/%s" %(year),
        DEC_23: "12/23/%s" %(year),
        DEC_24: "12/24/%s" %(year),
        DEC_25: "12/25/%s" %(year),
        DEC_26: "12/26/%s" %(year),
        DEC_27: "12/27/%s" %(year),
        DEC_28: "12/28/%s" %(year),
        DEC_29: "12/29/%s" %(year),
        DEC_30: "12/30/%s" %(year),
        DEC_31: "12/31/%s" %(year),
        
    }
    y = int(currentDT.year) - int(year)
        
    if month == "January" or month == "1":
        month = "1"
    elif month == "February" or month == "2":
        month = "2"
    elif month == "March" or month == "3":
        month = "3"
    elif month == "April" or month == "4":
        month = "4"
    elif month == "May" or month == "7":
        month = "5"
    elif month == "June" or month == "6":
        month = "6"
    elif month == "July" or month == "7": 
        month = "7"
    elif month == "August" or month == "8":
        month = "8"
    elif month == "September" or month == "9":
        month = "9"
    elif month == "October" or month == "10":
        month = "10"
    elif month == "November" or month == "11":
        month = "11"
    elif month == "December" or month == "12":
        month = "12"
    else:
        print("Please print a month")
        birth_algorithm()
        
    if int(month) > int(currentDT.month):
        y -= 1
    elif int(month) == int(currentDT.month):
        if int(day) > int(currentDT.day):
            y -= 1
            
        elif int(day) == int(currentDT.day):
            print("Happy Birthday!")
        else:
            y += 0
    elif int(month) < int(currentDT.month) and y < 1:
        m = int(currentDT.month) - int(month)
    else:
        y += 0
    time.sleep(2)
    print()
    print()
    print("You are %s years old" %(y))
        
    birth_date = datetime.datetime(int(year),int(month),int(day))
    day_alive = (currentDT - birth_date).days
    time.sleep(2)
    print()
    print("You are %s days old" %(day_alive))
    
    total = 0
    value = day_alive
    total_year = 0
    while value % 1000 != 0:
        value += 1
        total += 1
        if total/365 >= 1:
            total_year += 1
        else:
            if total_year >= 1:
                years = "You are more than a year away."
            elif total_year <= 1:
                years = "You are almost there"
            else:
                years = "Today must be your milestone!"
                
    time.sleep(2)
    print()
    print("For your %s day birthday, it is %s days left"%(value,total))
    birth = "%s/%s/%s" %(month, day, year)
    #print(years)
    time.sleep(2)
    print()
    holidays = holiday.keys()[holiday.values().index(birth)] #holds the code for getting data frmo the dictionary
    print("You were born on %s" %(holidays))
    time.sleep(2)
    print()
    if month == "1": #explains what zodiac symbol you are
        if int(day) >= 19:
            print("You are an Aquarius")
            zodiac = "Aquarius"
        else:
            print("You are a Capricorn")
            zodiac = "Capricorn"
    elif month == "2":
        if int(day) >= 19:
            print("You are a Pisces")
            zodiac = "Pisces"
        else:
            print("You are a Aquarius")
            zodiac = "Aquarius"
    elif month == "3":
        if int(day) >= 21:
            print("You are an Aries")
            zodiac = "Aries"
        else:
            print("You are a Pisces")
            zodiac = "Pisces"
    elif month == "4":
        if int(day) >= 20:
            print("You are a Taurus")
            zodiac = "Taurus"
        else:
            print("You are an Aries")
            zodiac = "Aries"
    elif month == "7":
        if int(day) >= 21:
            print("You are a Gemini")
            zodiac = "Gemini"
        else:
            print("You are a Taurus")
            zodiac = "Taurus"
    elif month == "6":
        if int(day) >= 21:
            print("You are a Cancer")
            zodiac = "Cancer"
        else:
            print("You are a Gemini")
            zodiac = "Gemini"
    elif month == "7":
        if int(day) >= 23:
            print("You are a Leo")
            zodiac = "Leo"
        else:
            print("You are a Cancer")
            zodiac = "Cancer"
    elif month == "8":
        if int(day) >= 23:
            print("You are a Virgo")
            zodiac = "Virgo"
        else:
            print("You are a Leo")
            zodiac = "Leo"
    elif month == "9":
        if int(day) >= 23:
            print("You are a Libra")
            zodiac = "Libra"
        else:
            print("You are a Virgo")
            zodiac = "Virgo"
    elif month == "10":
        if int(day) >= 23:
            print("You are a Scorpio")
            zodiac = "Scorpio"
        else:
            print("You are a Libra")
            zodiac = "Libra"
    elif month == "11":
        if int(day) >= 22:
            print("You are a Sagittarius")
            zodiac = "Sagittarius"
        else:
            print("You are a Scorpio")
            zodiac = "Scorpio"
    else:
        if int(day) >= 22:
            print("You are a Capricorn")
            zodiac = "Capricorn"
        else:
            print("You are a Sagittarius")
            zodiac = "Sagittarius"
    
            
title() #runs the title function
def algorithm():
    """
    The function packages data that will be able to allow the user to determine 
    if they want to save data, learn about a date or leave the code using raw_inputs
    and function calling.
    """
    save = raw_input("Would you like to save birthday or learn about your birthday or exit (save/learn/exit): ")
    if save == 'save':
        save_birthday()
    elif save == 'exit':
        return
    elif save == 'learn':
        birth_algorithm()
    else:
        print("Please select the right option")
    
def save_birthday():
    """
    This function hold data that allows the user to be able to save data on a birthday in a text file using the with command and raw_inputs
    """
    name = raw_input("Enter your name: ")
    birthday = raw_input("Enter your birthday: ")
    file = raw_input("File name: ")
    with open("./" + file + ".txt", 'a') as f:
        f.write(name + " - " + birthday + "\n")
    print("Birthday saved to the file " + file + ".txt \n" )
    algorithm()
algorithm()