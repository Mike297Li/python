dict={"A":"Newfoundland","B":"Nova Scotia","C":"Prince Edward Island","E":"New Brunswick",
      "G":"Quebec","H":"Quebec","J":"Quebec","K":"Ontario","L":"Ontario","M":"Ontario","N":"Ontario","P":"Ontario",
      "R":"Manitoba","S":"Saskatchewan","T":"Alberta","V":"British Columbia","X":"Nunavut or Northwest Territories",
      "Y":"Yukon"}

if "A" in dict:
    print(dict["X"])

# listInvalid=["D", "F", "I","O", "Q", "U", "W","Z"]
# postcode=input("please enter a postal code")
# provice=dict.get(postcode[0])
# # IN CASE postcode[1] will have error
# if len(postcode)<=1:
#     print("your postal code is too short")
# # The second character in a postal code identifies whether the address is rural or urban. If that
# # character is a 0 then the address is rural otherwise it is urban.
# # Display a meaningful error message if the postal code begins with an invalid character.
# elif listInvalid.__contains__(postcode[0]) or provice==None:
#     print("your postal code begins with an invalid character")
# else:
#     print(f"the postal code is from an rural address in {provice}") if postcode[1]=="0"  else print(f"the postal code is from an urban address in {provice}")