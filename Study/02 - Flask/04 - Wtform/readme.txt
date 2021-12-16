# This project demonstrates how to use form validation
# Below some notes to make things work fine

1) in the html form, let action empty so the post goes to the caller route
2) use novalidate in the form definition otherwise custom messages does not work (waste some time here)
3) to create custon validate, follow below rules:
    a. custom validation is a method defined in the class definition
    b. must be named validate_[fieldname] and receive field as parameter.ex: validate_username(self, field):
    c. the function must raise an exception. ex: raise ValidationError("Username é obrigatório")
    d. it is not necessary to call this function anyware
4) 
5) 

