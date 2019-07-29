function hasClass(element, className) {
    return (' ' + element.className + ' ').indexOf(' ' + className+ ' ') > -1;
}




function toggle_backend(id) {
    var xhr = new XMLHttpRequest();
    
    xhr.open('POST', '/toggle/' + id);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
           item = JSON.parse(xhr.responseText);
           set_strikethrough('item' + id, item.done)
        }
        else if (xhr.status !== 200) {
            alert('Fail');
        }
    };
    xhr.send();
}



function set_strikethrough(elem_id, is_done) {
    elem = document.getElementById(elem_id);
    if (is_done) {
        elem.classList.add("done"); 
    } else {
        elem.classList.remove("done");
    }
}

