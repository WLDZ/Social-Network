document.addEventListener('DOMContentLoaded', function() {

// This loop iterates through each button, extracts the user_id from the button's id,
// and calls the change_button_color function


  document.querySelectorAll(".vdislike").forEach(button => {  //event listener on button class instad of a particular button
    {

    user_id = button.id.split("dl")[0];         
    change_dislike_button_color(user_id)

    }   
})


    
  document.querySelectorAll(".vdislike").forEach(button => {  //event listener on button class instad of a particular button
        button.onclick =function(){
        
          user_id = button.id.split("dl")[0];
          disliked(user_id)
          
        }   
    })

});




async function getDisikeStatus(user_id) {
  const response  = await fetch(`/check_dislike/${user_id}/`)
  const data = await response.json();
  //the addData adds the object "data" to an array
  // console.log(`output from getDisikeStatus function: ${data} }`)
  return data
}

async function disliked(user_id) {
  
  let result =   await getDisikeStatus(user_id);

 
  if (result == true)  // true means not disliked yet
  {
    fetch('/dislike/', {
      method: 'POST',
      body: JSON.stringify({
      postid: user_id  
      })
      })
      .then(response => response.json())
      .then(result => {
        
      });

      likes_count = parseInt(document.getElementById(`lbd${user_id}`).innerHTML,10)

      // console.log(document.getElementById(`lbd${user_id}`).innerHTML)
      document.getElementById(`lbd${user_id}`).innerHTML =likes_count+=1
      document.getElementById(`${user_id}dl`).style.backgroundColor = "grey" 
      
      
  
  }
  else{
    fetch('/undislike/', {  // if the post is already disliked by the user and user want to undislike it
      method: 'POST',
      body: JSON.stringify({
      postid: user_id  
      })
      })
      .then(response => response.json())
      .then(result => {
      });

      likes_count = parseInt(document.getElementById(`lbd${user_id}`).innerHTML,10)
      document.getElementById(`lbd${user_id}`).innerHTML =likes_count-=1
      document.getElementById(`${user_id}dl`).style.backgroundColor = "#FF9C92"

  }
  
}



async function change_dislike_button_color(user_id) {
  
    let result =   await getDisikeStatus(user_id);
   
    if (result == false)
    {
  
      document.getElementById(`${user_id}dl`).style.backgroundColor = "grey" 
    }
    
  }