function t3(s){
    const Http = new XMLHttpRequest();
    const url='https://gracesite.github.io/r/hello.html';
    Http.open("GET", url);
    Http.send();
    
    Http.onreadystatechange = (e) => {
      console.log(Http.responseText)
    }
    return Http.responseText
};
var str1 = t3(msg);
document.getElementById('tile_2').innerText = str1;
