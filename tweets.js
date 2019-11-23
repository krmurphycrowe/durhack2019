function getPage(pg){
    const Http = new XMLHttpRequest();
    let url = "https://bowis-jownson.herokuapp.com/api/v1/tweets?page=" + pg;
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=(e)=>{
        let res = Http.responseText;
        let tweetArray = JSON.parse(res);
        console.log(typeof(tweetArray));
        console.log(tweetArray);
    }
}