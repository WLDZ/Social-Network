document.addEventListener('DOMContentLoaded', function() {
 

    
    
        
        document.querySelectorAll(".vlike").forEach(button => {  //event listener on button class instad of a particular button
          button.onclick =function(){
          
            user_id = button.id.split("l")[0];
           
            like3(user_id);  //current user id is being managed through django view
      
          }
    
    
    
        
      })
        
      })
    
    
    
async function my_async5(user_id) {
    
const response  = await fetch(`/check_like/${user_id}/`)
const data = await response.json();
//the addData adds the object "data" to an array
return data
    }   

async function like3(user_id)
{
    let result =   await my_async5(user_id);

    
    
    console.log(result)
    if (result == true)
    {
    fetch('/like/', {
        method: 'POST',
        body: JSON.stringify({
        postid: user_id  
        })
        })
        .then(response => response.json())
        .then(result => {
        
        });
        likes_count = parseInt(document.getElementById(`lbl${user_id}`).innerHTML,10)
        document.getElementById(`lbl${user_id}`).innerHTML =likes_count+=1
        document.getElementById(`${user_id}l`).style.color = "blue" 
    
    }


    else{
        
        
        unlike_post(user_id)

    }
}

    
    
    

      
function unlike_post(user_id)
{
    fetch('/unlike/', {
        method: 'POST',
        body: JSON.stringify({
        postid: user_id  
        })
        })
        .then(response => response.json())
        .then(result => {

        
        });

    likes_count = parseInt(document.getElementById(`lbl${user_id}`).innerHTML,10)
    document.getElementById(`lbl${user_id}`).innerHTML =likes_count-=1
    document.getElementById(`${user_id}l`).style.color = "#26a69a"

}
    
    
      
    