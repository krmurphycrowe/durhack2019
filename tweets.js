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
        console.log(tweetArray);
        let links = [];
        let re = new RegExp("https:[^ ]*");
        for(let x = 0; x < 20; x++){
            let index = tweetArray[x].search(re);
            if (index == -1){
                links[x] = "";
            }
            else{
                links[x] = tweetArray[x].slice(index,tweetArray[x].length);
                tweetArray[x] = tweetArray[x].slice(0,index);
            }
        }
        let i = 1
        while(i <= 20){
            if (tweetArray[i-1] == "EMPTY"){
                document.getElementById("b"+i.toString()).innerHTML = "";
                document.getElementById("t"+i.toString()).innerHTML = "";
                document.getElementById("img"+i.toString()).src="";
            }
            else{
                document.getElementById("b"+i.toString()).innerHTML = "@BowisJownson";
                document.getElementById("t"+i.toString()).innerHTML = tweetArray[i-1];
                document.getElementById("img"+i.toString()).src="buwuis.jpg";
                document.getElementById("img"+i.toString()).width="100";
            }
            i++;
        }
    }
}