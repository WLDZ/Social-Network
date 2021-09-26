document.addEventListener('DOMContentLoaded', function() {
 

    
    document.querySelector('#follow-button').addEventListener('click',follow_unfollow);
    
       
       document.querySelectorAll('.edit').forEach(button => {
         button.onclick =function(){
    
          post_id = button.value
          document.getElementById(post_id+'p').readOnly = false;
           button.style.display = "none"
           document.getElementById(post_id+'b').style.display = 'block';
    
         }
       })

});


function follow_unfollow()
{

    follow_value = document.querySelector('#follow-button').value
    console.log(follow_value)
    if (follow_value == '')
    {
      fetch('/follow/', {
        method: 'POST',
        body: JSON.stringify({
        follower_id: document.querySelector('#e').value
        })
        })
        .then(response => response.json())
        .then(result => {
        });

        document.querySelector('#follow-button').value = 'Unfollow'
        document.querySelector('#follow-button').innerHTML ="Unfollow"

       
        follow_count = parseInt(document.getElementById("followcount").innerHTML,10)
        document.getElementById("followcount").innerHTML =follow_count+=1
  

    }

   else if (follow_value == 'Unfollow')
    {

      fetch('/unfollow/', {
        method: 'POST',
        body: JSON.stringify({
        follower_id: document.querySelector('#e').value
        })
        })
        .then(response => response.json())
        .then(result => {
        });

        document.querySelector('#follow-button').value = ''
        document.querySelector('#follow-button').innerHTML ="Follow"


        follow_count = parseInt(document.getElementById("followcount").innerHTML,10)
        document.getElementById("followcount").innerHTML =follow_count-=1
    }
    
    
}
