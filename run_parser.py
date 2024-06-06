import os
from brand_parser import BottegaVenetaParser, GucciParser, FendiParser, BallyParser, StellaProductParser, Chloe_Parser, \
    GivenchyProductParser, CanadaGooseProductParser, IsabelMarantParser, MCM_Parser, CultGaiaProductParser, \
    GoldenGooseProductParser, FendiParser, BalenciagaParser, SaintLaurentParser, AlexanderMcqueenParser, \
    Dolce_Gabbana_Parser, StoneIslandParser, EtroProductParser, MonclerParser, BalmainProductParser, \
    VersaceProductParser, FerragamoProductParser, BurberryParser, KenzoParser, VejaProductParser, JimmyChooParser, \
    BrunelloCucinelliParser, DSquaredParser, CelineParser, LoroPianaParser, MarniParser, PradaParser, TodsParser, \
    ValentinoParser, JacquemusParser, LouboutinParser, PalmAngelsParser, MooseKnucklesParser, AcneStudiosParser, \
    TheRowParser, ManoloBlahnikParser, GianvitoRossiParser, MiuMiuParser, BirkenstockParser, AquazzuraParser, \
    OffWhiteProductParser

#Folder name for output
output_directory_path = "parser-output"
#directory_path = 'brands_html/bottega_veneta'
##Bottega Veneta Parser METHOD 1##

##SINGLE FILE RUN##
#input_file_path = '/Users/samuelshlyam/PycharmProjects/pythonProject1/site-parsing/internal_html/bottega_veneta'
#category = os.path.splitext(input_file_path)[0]  # Use the filename as the category
##Uncomment to run##
#bottega_parser_output = bottega_parser.parse_website(input_file_path, category)
#bottega_parser.write_to_csv(bottega_parser_output)

##MULTIPLE FILE RUN, PASS DIRECTORY PATH
##Comment to run single file##
bottega_parser = BottegaVenetaParser(output_directory_path)
directory_path = r'/Users/samuelshlyam/PycharmProjects/pythonProject1/site-parsing/internal_html/bottega_veneta'
bottega_parser.parse_directory(directory_path)


#GUCCI PRODUCT FETCH METHOD 2##

#gucci_parser = GucciParser()

#gucci_categories_womens = ['women-shoes','women-handbags','women-accessories-lifestyle-bags-and-luggage','women-readytowear','women-accessories-wallets','women-accessories','jewelry-watches-watches-women', 'women-accessories-belts','women-accessories-silks-and-scarves','women-accessories-hats-and-gloves']
#gucci_categories_mens = ['men-bags', 'men-bags-luggage','men-readytowear','men-shoes','men-accessories-wallets','men-accessories-hats-and-gloves','men-accessories-belts','men-eyewear','jewelry-watches-watches-men','men-accessories']
#combined_gucci_categories = ['men-bags', 'men-bags-luggage','men-readytowear','men-shoes','men-accessories-wallets','men-accessories-hats-and-gloves','men-accessories-belts','men-eyewear','jewelry-watches-watches-men','men-accessories','women-shoes','women-handbags','women-accessories-lifestyle-bags-and-luggage','women-readytowear','women-accessories-wallets','women-accessories','jewelry-watches-watches-women', 'women-accessories-belts','women-accessories-silks-and-scarves','women-accessories-hats-and-gloves']
##UNCOMMENT TO RUN, COMMENT OTHER PARSERS, to avoid multi run##
#gucci_parser.process_categories(combined_gucci_categories)


##START FENDI PARSER##
#directory_path = 'internal_html/fendi'
#fendi_parser = FendiParser(output_directory_path)
#fendi_parser.parse_directory(directory_path)
#Fendi END



###BALLY START
#bally_parser = BallyParser()
#category_list = ['men-sale.json?', 'women-sale.json?', 'men.json?', 'women.json?']
# bally_parser.process_categories(category_list)

#BALLY END

#STELLA START
#stella_parser = StellaProductParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\stella_mccartney'
#stella_parser.parse_directory(directory_path)
#stella end

#Off White START#
#OffWhiteParser = OffWhiteProductParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\off_white'
#OffWhiteParser.parse_directory(directory_path)
#Off White end

#givenchy START
#givenchy_parser = GivenchyProductParser(output_directory_path)
##Comment to run single file##
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\givenchy'
#givenchy_parser.parse_directory(directory_path)
#givenchy END


#Canada Goose Start
#canada_goose_parser = CanadaGooseProductParser(output_directory_path)
#directory_path = r'/Users/samuelshlyam/PycharmProjects/pythonProject1/site-parsing/internal_html/canada_goose'
#canada_goose_parser.parse_directory(directory_path)
#Canada Goose END

#Veja Start
VejaParser = VejaProductParser(output_directory_path)
directory_path = r'/Users/samuelshlyam/PycharmProjects/pythonProject1/site-parsing/internal_html/veja'
VejaParser.parse_directory(directory_path)
#Veja End



#Isabel Marant Start
#Isabel_Marant_Parser = IsabelMarantParser(output_directory_path)
##Comment to run single file##
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\isabel_marant'
#Isabel_Marant_Parser.parse_directory(directory_path)
#Isabel Marant End

#Chloe Start
#Chloe_parser=Chloe_Parser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\chloe'
#Chloe_parser.parse_directory(directory_path)
#Chloe End

#MCM start
#mcm_parser=MCM_Parser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\mcm'
#mcm_parser.parse_directory(directory_path)
#MCM End

#Cult Gaia Start
#cult_gaia_parser=CultGaiaProductParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\cult_gaia'
#cult_gaia_parser.parse_directory(directory_path)
#Cult Gaia end

#Golden Goose Start
#Golden_Goose_ProductParser=GoldenGooseProductParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\golden_goose'
#Golden_Goose_ProductParser.parse_directory(directory_path)
#Golden Goose End

#Balenciaga Start
#balenciaga_Parser=BalenciagaParser(output_directory_path)
#directory_path = r'/Users/samuelshlyam/PycharmProjects/pythonProject1/site-parsing/internal_html/balenciaga'
#balenciaga_Parser.parse_directory(directory_path)
#Balenciaga End


#YSL Start
#YSL_Parser=SaintLaurentParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\saint-laurent'
#YSL_Parser.parse_directory(directory_path)
#YSL End




#Alexander Mcqueen Start
#women_categories = ['w-ready-to-wear','W-All-Shoes' ,'W-All-Bags','W-All-Accessories','w-jewellery' ]  # Assuming you have a list of categories
#men_categories = ['M-All-Ready-to-Wear','M-Shoes','M-All-Accessories', 'm-jewellery','M-Bags']
#women_base_url = "https://www.alexandermcqueen.com/api/v1/category/women?locale=en-us&categoryIds={clothing_category}&page={page}"
#men_base_url = "https://www.alexandermcqueen.com/api/v1/category/men?locale=en-us&categoryIds={clothing_category}&page={page}"
#AlexMcqueenMenParser=AlexanderMcqueenParser(men_base_url)
#AlexMcqueenWomenParser=AlexanderMcqueenParser(women_base_url)
#AlexMcqueenMenParser.process_categories(men_categories)
#AlexMcqueenWomenParser.process_categories(women_categories)
#Alexander Mcqueen End

#Dolce Start
#bearer_token= "eyJ2ZXIiOiIxLjAiLCJqa3UiOiJzbGFzL3Byb2QvYmtkYl9wcmQiLCJraWQiOiI4ZTA2MGIwZi0yYjZlLTQ5NWQtOGY4Ny04NDUxOWE3NmRhOWEiLCJ0eXAiOiJqd3QiLCJjbHYiOiJKMi4zLjQiLCJhbGciOiJFUzI1NiJ9.eyJhdXQiOiJHVUlEIiwic2NwIjoic2ZjYy5zaG9wcGVyLW15YWNjb3VudC5iYXNrZXRzIHNmY2Muc2hvcHBlci1kaXNjb3Zlcnktc2VhcmNoIHNmY2Muc2hvcHBlci1teWFjY291bnQucGF5bWVudGluc3RydW1lbnRzIHNmY2Muc2hvcHBlci1jdXN0b21lcnMubG9naW4gc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5vcmRlcnMgc2ZjYy5zaG9wcGVyLXByb2R1Y3RsaXN0cyBzZmNjLnNob3BwZXItcHJvbW90aW9ucyBzZmNjLnNob3BwZXIuc3RvcmVzIHNmY2Mub3JkZXJzLnJ3IHNmY2Muc2Vzc2lvbl9icmlkZ2Ugc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wYXltZW50aW5zdHJ1bWVudHMucncgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wcm9kdWN0bGlzdHMgc2ZjYy5zaG9wcGVyLWNhdGVnb3JpZXMgc2ZjYy5zaG9wcGVyLW15YWNjb3VudCBzZmNjLnNob3BwZXItbXlhY2NvdW50LmFkZHJlc3NlcyBzZmNjLnNob3BwZXItcHJvZHVjdHMgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5ydyBzZmNjLnNob3BwZXItY29udGV4dC5ydyBzZmNjLnNob3BwZXItYmFza2V0cy1vcmRlcnMgc2ZjYy5zaG9wcGVyLWN1c3RvbWVycy5yZWdpc3RlciBzZmNjLnNob3BwZXItbXlhY2NvdW50LmFkZHJlc3Nlcy5ydyBzZmNjLnNob3BwZXItbXlhY2NvdW50LnByb2R1Y3RsaXN0cy5ydyBzZmNjLnNob3BwZXItcHJvZHVjdCBzZmNjLnNob3BwZXItYmFza2V0cy1vcmRlcnMucncgc2ZjYy5zaG9wcGVyLWdpZnQtY2VydGlmaWNhdGVzIHNmY2Muc2hvcHBlci1wcm9kdWN0LXNlYXJjaCIsInN1YiI6ImNjLXNsYXM6OmJrZGJfcHJkOjpzY2lkOjAxYzNhMjlmLTMzNmMtNDlkNS04ZWJlLWMxMzNmZjk4Mjk0NTo6dXNpZDo3NzM1MDMyNi1mNjMxLTQxZjItOWE4MC01MzQ3MjBkNDVlMTEiLCJjdHgiOiJzbGFzIiwiaXNzIjoic2xhcy9wcm9kL2JrZGJfcHJkIiwiaXN0IjoxLCJkbnQiOiIwIiwiYXVkIjoiY29tbWVyY2VjbG91ZC9wcm9kL2JrZGJfcHJkIiwibmJmIjoxNzE3MDIxOTA5LCJzdHkiOiJVc2VyIiwiaXNiIjoidWlkbzpzbGFzOjp1cG46R3Vlc3Q6OnVpZG46R3Vlc3QgVXNlcjo6Z2NpZDpiY2xYQVhscmFYa0h3UnhId1hrcVlZa3V3Vzo6Y2hpZDogIiwiZXhwIjoxNzE3MDIzNzM5LCJpYXQiOjE3MTcwMjE5MzksImp0aSI6IkMyQzc3NTc1MzE4MjAtMTYwMDU0NTkwNzE4MTUwNDA4MzQ1MzE2NDgifQ.cAcmEZb_x-YVfEpSn-MrIcO1UjtaL9wdG9QudX7RpdZHoGQxSNq-OVqKgyJpu3f7wPw1tT4EYN_k_AsBv_GsLg"
#categories = ['cgid%3Dwomen-bags', 'cgid%3Dwomen-apparel', 'cgid%3Djewellry-for-her', 'cgid%3Dwomen-shoes',
#              'cgid%3Dwomen-accessories', 'cgid%3Dwomen-accessories-sunglasses', 'cgid%3Dmen-apparel',
#              'cgid%3Dmen-tailoring', 'cgid%3Dmen-bags', 'cgid%3Dmen-shoes', 'cgid%3Dmen-accessories',
#              'cgid%3Dmen-accessories-sunglasses', 'cgid%3Djewellry-for-him']
#Dolce_Parser=Dolce_Gabbana_Parser()
#Dolce_Parser.process_categories(categories,bearer_token)
#Dolce End

#Stone Island Start
#StoneParser = StoneIslandParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\stone_island'
#StoneParser.parse_directory(directory_path)
#Stone Island End


#Etro Start
#EtroParser = EtroProductParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\etro'
#EtroParser.parse_directory(directory_path)
#Etro End

#Balmain Start
#BalmainParser = BalmainProductParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\balmain'
#BalmainParser.parse_directory(directory_path)
#Balmain End


#Moncler Start
#cookie= r'dwanonymous_6ff516fc64e5194a34356fc83db5a3b8=adhFdfPauAzgggM6avxKkbPflW; __cq_dnt=1; dw_dnt=1; dw_locale=en_US; rskxRunCookie=0; rCookie=36ssfsyb702aciihw01iwhlwryawsn; _fwb=1975g8QlX9fyClXBHhkbN6F.1716994684493; OptanonAlertBoxClosed=2024-05-29T14:58:07.857Z; OneTrustChoices=%7B%22action%22%3A%22ConsentTracking-OneTrust%22%2C%22queryString%22%3A%22optanonag%3D%252CC0001%252CH1%252CH7%252CH17%252CH8%252CH9%252C%22%2C%22locale%22%3A%22en_US%22%2C%22originalUri%22%3A%22https%3A%2F%2Fwww.moncler.com%2Fen-us%2Fconsent%2Fonetrust%2F%3Foptanonag%3D%252CC0001%252CH1%252CH7%252CH17%252CH8%252CH9%252C%22%2C%22success%22%3Atrue%2C%22cqtracking%22%3Afalse%2C%22gatraking%22%3Afalse%2C%22mcTraking%22%3Afalse%2C%22raTraking%22%3Afalse%2C%22meTracking%22%3Afalse%7D; sid=o0Jf9kgEuinJ59Dskka4dzkEcro3HfHBqOk; dwsid=F-y7KdVQqfreAnM4Olq2Jo2qlmWqSeISvwyA5sySefVH5gjtstEPYlHZ334dmY2aGrVN19QleeoR_K8W6_I0JQ==; lastRskxRun=1717084755902; RT="sl=1&ss=1717084737280&tt=2276&obo=0&sh=1717084739557%3D1%3A0%3A2276&dm=moncler.com&si=mkpaxe8itra&rl=1"; OptanonConsent=isGpcEnabled=0&datestamp=Thu+May+30+2024+11%3A59%3A16+GMT-0400+(Eastern+Daylight+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&consentId=78b98805-e066-4a97-83ef-75f4f2c60f4a&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0%2CC0003%3A0&hosts=H1%3A1%2CH7%3A1%2CH17%3A1%2CH8%3A1%2CH9%3A1%2CH15%3A0%2CH43%3A0%2CH18%3A0%2CH42%3A0%2CH48%3A0%2CH19%3A0%2CH46%3A0%2CH2%3A0%2CH20%3A0%2CH21%3A0%2CH40%3A0%2CH22%3A0%2CH23%3A0%2CH44%3A0%2CH24%3A0%2CH5%3A0%2CH25%3A0%2CH6%3A0%2CH26%3A0%2CH27%3A0%2CH41%3A0%2CH16%3A0%2CH28%3A0%2CH29%3A0%2CH30%3A0%2CH31%3A0%2CH49%3A0%2CH32%3A0%2CH45%3A0%2CH33%3A0%2CH34%3A0%2CH39%3A0%2CH35%3A0%2CH13%3A0%2CH36%3A0%2CH38%3A0%2CH37%3A0%2CH47%3A0%2CH50%3A0%2CH4%3A0%2CH11%3A0&genVendors=V1%3A0%2C&geolocation=US%3BNY&AwaitingReconsent=false'
#categories = ['']
#Moncler_Parser=MonclerParser()
#Moncler_Parser.process_categories(categories,cookie)
#Moncler End

#Versace Start
#VersaceParser = VersaceProductParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\versace'
#VersaceParser.parse_directory(directory_path)
#Versace End

#Ferragamo Start
#FerragamoParser = FerragamoProductParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\ferragamo'
#FerragamoParser.parse_directory(directory_path)
#Ferragamo End


#Burberry Start
#burberryParser = BurberryParser(output_directory_path)
#directory_path = r'/Users/samuelshlyam/PycharmProjects/pythonProject1/site-parsing/internal_html/burberry'
#burberryParser.parse_directory(directory_path)
#Burberry End


#Kenzo Start
#kenzoParser = KenzoParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\kenzo'
#kenzoParser.parse_directory(directory_path)
#Kenzo End


#Jimmy Choo Start
#jimmyChooParser = JimmyChooParser(output_directory_path)
#directory_path = r'/Users/samuelshlyam/PycharmProjects/pythonProject1/site-parsing/internal_html/jimmy_choo'
#jimmyChooParser.parse_directory(directory_path)
#JimmyChoo End


#Brunello Cucinelli Start
#brunelloCucinelliParser = BrunelloCucinelliParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\brunello_cucinelli'
#brunelloCucinelliParser.parse_directory(directory_path)
#Brunello Cucinelli End

#DSquared2 Start
#dSquaredParser = DSquaredParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\dsquared2'
#dSquaredParser.parse_directory(directory_path)
#DSquared2 End


#Celine Start
#celineParser = CelineParser(output_directory_path)
#directory_path = r'/Users/samuelshlyam/PycharmProjects/pythonProject1/site-parsing/internal_html/celine'
#celineParser.parse_directory(directory_path)
#Celine End


#Loro Piana Start
#categories=['L1_MEN','L1_WOM','L2_MEN_ACCESSORIES','L2_WOM_LG','L2_WOM_ACCESSORIES','L2_SHOES_WOM','L2_WOM_SLG','L2_SHOES_MAN',]
#LoroParser=LoroPianaParser()
#LoroParser.process_categories(categories)
#Loro Piana End


#Marni Start
#marniParser = MarniParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\marni'
#marniParser.parse_directory(directory_path)
#Marni End

#Prada Start
#pradaParser = PradaParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\prada'
#pradaParser.parse_directory(directory_path)
#Prada End

#Tods Start
#todsParser = TodsParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\tods'
#todsParser.parse_directory(directory_path)
#Tods End

#Valentino Start
#valentinoParser = ValentinoParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\valentino'
#valentinoParser.parse_directory(directory_path)
#Valentino End

#Jacquemus Start
#jacquemusParser = JacquemusParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\jacquemus'
#jacquemusParser.parse_directory(directory_path)
#Jacquemus End

#Louboutin Start
#louboutinParser = LouboutinParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\louboutin'
#louboutinParser.parse_directory(directory_path)
#Louboutin End

#Palm Angels Start
#palmAngelsParser = PalmAngelsParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\palm_angels'
#palmAngelsParser.parse_directory(directory_path)
#PalmAngels End

#Moose Knuckles Start
#mooseKnucklesParser = MooseKnucklesParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\moose_knuckles'
#mooseKnucklesParser.parse_directory(directory_path)
#Moose Knuckles End

#Acne Studios Start
#acneStudiosParser = AcneStudiosParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\acne_studios'
#acneStudiosParser.parse_directory(directory_path)
#Acne Studios End

#The Row Start
#theRowParser = TheRowParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\the_row'
#theRowParser.parse_directory(directory_path)
#The Row End

#Manolo Blahnik Start
#manoloBlahnikParser = ManoloBlahnikParser(output_directory_path)
#directory_path = r'/Users/samuelshlyam/PycharmProjects/pythonProject1/site-parsing/internal_html/manolo_blahnik'
#manoloBlahnikParser.parse_directory(directory_path)
#Manolo Blahnik End

#Gianvito Rossi Start
#gianvitoRossiParser = GianvitoRossiParser(output_directory_path)
#directory_path = r'/Users/samuelshlyam/PycharmProjects/pythonProject1/site-parsing/internal_html/gianvito_rossi'
#gianvitoRossiParser.parse_directory(directory_path)
#Gianvito Rossi End

#Miu Miu Start
#miuMiuParser = MiuMiuParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\miu_miu'
#miuMiuParser.parse_directory(directory_path)
#Gianvito Rossi End

#Birkenstock Start
#birkenstockParser = BirkenstockParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\birkenstock'
#birkenstockParser.parse_directory(directory_path)
#Birkenstock End

#Aquazzura Start
#aquazzuraParser = AquazzuraParser(output_directory_path)
#directory_path = r'C:\Users\User\PycharmProjects\pythonProject\site-parsing\internal_html\aquazzura'
#aquazzuraParser.parse_directory(directory_path)
#Aquazzura End

