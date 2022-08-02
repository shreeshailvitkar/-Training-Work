var booksMenu = ['COD','MOD','GOD'];

function addBook()
{
    var add_form = '<form><label for="book-name">Name of Book:</label><br><input type="text"  name="book-name" id="book-name" ><br><label for="Author of Book">Author of Book:</label><br><input type="text" ><br><br><button type="button" class="button" onClick="add_book()">Add Book</button></form> '
    var content =  document.getElementById("details").innerHTML = add_form;
    function add_book()
    {
        var book_name = document.getElementById("book-name");
        alert(book_name);
    }
    
}

function listOfBook()
{
    //var books = '<ul><li>Rich Dad</li><li>Poor Dad</li><li>MAsters of Himalya</li></ul>'
    var content =  document.getElementById("details").innerHTML = booksMenu;

    

}


function editBook()
{
    var content = '<h3>Click on book name to edit book</h3><br><br><p contenteditable="true"><b>Rich dad <br>poor dad <br>Masters of Himalya <b><br></p>'
    var content =  document.getElementById("details").innerHTML = content;
}


function removeBook()
{
    var remove_form = '<form><label for="book-name">Name of Book:</label><br><input type="text"  name="book-name" ><br><br><input type="text" ><br><br><button type="button" class="button">Remove Book</button></form> '
   var content =  document.getElementById("details").innerHTML = remove_form;
}
