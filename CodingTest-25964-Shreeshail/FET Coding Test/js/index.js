function book_ticket()
{
    var name = document.getElementById('name').value
    var email1 = document.getElementById('email1').value
    var email2 = document.getElementById('email2').value
    var stand = document.getElementById('stand').value
    var floor = document.getElementById('floor').value
    var valid = true

    if(name == '')
    {
        alert('Enter a Name')
        valid = false
    }else if(email1 == '')
    {
        alert('Enter email')
        valid = false
    }else if( email1 != email2)
    {
        alert('email not matching re-enter data')
        valid = false
    }else if(stand == 'Select Stand')
    {
        alert('select stand')
        valid = false
    }else if(stand == 'Select Floor')
    {
        alert('select floor')
        valid = false
    }

    var price = document.getElementById('price');
    var cal_price

    if(stand == 'PG' && floor == 'FF')
    {
        alert('selecting floor is not applicable keep blank')   
        valid = false
       
    }else if ( stand == 'PG' && floor == 'SF')
    {
        alert('selecting floor is not applicable keep blank')
        valid = false

    }else if ( stand == 'PG')
    {
        cal_price = 25000
        

    }else
    
    if ( stand == 'SHS' && floor == 'FF')
    {
        alert('selecting floor is not applicable keep blank')
        valid = false

    }else if ( stand == 'SHS' && floor == 'SF')
    {
        alert('selecting floor is not applicable keep blank')
        valid = false

    }else if(stand == 'SHS')
    {
        cal_price = 20000
    }else if(stand == 'NWS' && floor == 'FF')
    {
        cal_price = 6000
    }else if(stand == 'NWS' && floor == 'SF')
    {
        cal_price = 2000
    }else if(stand == 'ES' && floor == 'FF')
    {
        cal_price = 3000
    }else if (stand == 'ES' && floor == 'SF')
    {
        cal_price = 1000
    }else
    {
        cal_price = 'Enter valide data'
    }

    
    
    if(valid == true)
    {
        price.value = cal_price;
        alert('All data entered is correct')
        

    }else
    {
        cal_price = 'please enter valide data'
        price.value = cal_price;
    }

    
       

}