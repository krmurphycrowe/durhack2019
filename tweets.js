function getPage(pg){
    const Http = new XMLHttpRequest();
    let url = "https://bowis-jownson.herokuapp.com/api/v1/tweets?page=" + pg;
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=(e)=>{
        let res = Http.responseText;
        let tweetArray = JSON.parse(res);
        while (tweetArray.length != 20){
            tweetArray.push("EMPTY");
        }
        console.log(typeof(tweetArray));
        console.log(tweetArray.length); 
        document.getElementById("tweet1").innerHTML = tweetArray[0];
    }
}