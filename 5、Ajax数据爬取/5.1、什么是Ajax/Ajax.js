var xmlhttp;

if (window.XMLHttpRequest) {
    xmlhttp = new XMLHttpRequest()
} else{//code for IE6, IE5
    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
}
xmlhttp.onreadstatechange=function(){
    if (xmlhttp.readState==4 && xmlhttp.status==200){
        document.getElementById("myDiv").innerHTML=xmlhttp.responeseText;
    }
}
xmlhttp.open("POST", "/ajax/", true);
xmlhttp.send()