var d = null
$(document).ready(() => {
    d = new Date();
})

$('#red').click(function() {
    var count = $('#red-counter').html()
    count++
    console.log(count)
    $('#red-counter').html(count)
    let n = new Date()
    let dif = Math.abs(n - d);
    let secs = ((dif % 60000) / 1000)
    alert(secs)
    $.post("{%url 'red' %}",
    {
        name: "Donald Duck",
        city: "Duckburg"
    },
    function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
    });
});

$('#blue').click(function() {
    var count = $('#blue-counter').html()
    count++
    console.log(count)
    $('#blue-counter').html(count)
    let n = new Date()
    let dif = Math.abs(n - d);
    let secs = ((dif % 60000) / 1000)
    alert(secs)
})
