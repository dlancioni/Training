# This project demonstrates how to use form validation
# Below some notes to make things work fine

1) in the html form, let action empty so the post goes to the caller route
2) IMPORTANT, use "novalidate" in the form definition otherwise custom messages does not work (you see standard message in english)
3) to create custon validate (for specific field):
    a. in the class form, define a method named validate_[fieldname] passing the field as parameter.ex: 
        validate_name(self, field), 
        validate_password(self, field)
    c. the function must raise an exception. ex: raise ValidationError("Username é obrigatório")
    d. it is not necessary to call this function anyware
4) to create custon validate (global, used in any form):
    a. create a regular python function ABOVE the form classes
    b. call the function in validors[] as you do with regular validators
    c. the function must raise an exception. ex: raise ValidationError("Username é obrigatório")
    d. IMPORTANT, you need chain function. First to pass input parameter, second to pass mandatory form/field parameters 
5) Dont forget to test if the form is validated in route that is mounting the form:
    a. if form.validate_on_submit():
6) Some validators (like Email) are not standard and must be installed via PIP command