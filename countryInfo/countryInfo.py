from countryinfo import CountryInfo
#My country Uruguay, search it
count=input("Enter your country : ")
country = CountryInfo(count)
print("Capital is : ", country.capital())
print("Currencies is : ", country.currencies())
print("Languages is : ", country.languages())
print("Borders are : ", country.borders())
print("Others names : ", country.alt_spellings())
print("UTC time is : ", country.timezones())
print("Wiki if you want to know more : ", country.wiki())



