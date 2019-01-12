var words=["Words","In","A","Box"];

function niceRegularBox(words){
  var LongestLen = findlongestWordLength(words);
  console.log("-".repeat(longestLen + 4))
  for(var i=0; i<words.length; i=i+1)
	{
    console.log("| " + words[i] + " ".repeat(longestLen - words[i].length) + " |");
  }
  console.log("-".repeat(longestLen + 4))
}

function longestWordLength(words){
  var maxLen = 0;
  for(var i=0; i<words.length; i=i+1)
	{
    if (words[i]length>maxLen){
      maxLen=words[i].length[i]
    }
  }
  return maxLen;
}
