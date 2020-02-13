function func_whattime(){
    return new Date().toTimeString();
};

var str1 = func_whattime();
document.getElementById('demo4').innerText = str1
