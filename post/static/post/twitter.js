$(function() {

});

function tweetPost()
{
    let username = document.getElementById("username");
    let tweetText = document.getElementById("tweet-text")
    alert ("User name: " + username.value + "\nText: " + tweetText.value);
    window.location.href = "main";
}
