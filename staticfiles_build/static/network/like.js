document.addEventListener('DOMContentLoaded', function() {
// This loop iterates through each button, extracts the user_id from the button's id,
// and calls the change_button_color function

  document.querySelectorAll(".olike, .like, .vlike").forEach(button => {  //event listener on button class instad of a particular button
    {

    user_id = button.id.split("l")[0];         
    change_button_color(user_id)

    }})


    document.querySelectorAll(".olike, .like, .vlike").forEach(button => {
        button.addEventListener("click", async () => {
            const user_id = button.id.split("l")[0];
            
            // Using try-catch to handle any errors that might occur during the asynchronous operations
            try {
                // Then, wait for the liked operation
                await liked(user_id);
            } catch (error) {
                console.error("Error in .olike, .like, .vlike button click:", error);
                // Handle error appropriately
            }
        });
    });
    
    
});

// Using async/await in the function signature
async function check_like(user_id) {
    const response = await fetch(`/check_like/${user_id}/`);
    const data = await response.json();
    return data;
}

// Using async/await in the function signature
async function liked(user_id) {
    try {
        const result = await check_like(user_id);

        if (result === true) {
            // Using async/await in the fetch call
            const response = await fetch('/like/', {
                method: 'POST',
                body: JSON.stringify({
                    postid: user_id
                })
            });
            // Using async/await to get the response data
            const data = await response.json();

            likes_count = parseInt(document.getElementById(`lbl${user_id}`).innerHTML, 10);
            document.getElementById(`lbl${user_id}`).innerHTML = likes_count += 1;
            document.getElementById(`${user_id}l`).style.color = "blue";
            document.getElementById(`${user_id}dl`).disabled = true;
        } else {
            // Using async/await in the fetch call
            const response = await fetch('/unlike/', {
                method: 'POST',
                body: JSON.stringify({
                    postid: user_id
                })
            });
            // Using async/await to get the response data
            const data = await response.json();

            likes_count = parseInt(document.getElementById(`lbl${user_id}`).innerHTML, 10);
            document.getElementById(`lbl${user_id}`).innerHTML = likes_count -= 1;
            document.getElementById(`${user_id}l`).style.color = "#26a69a";
            document.getElementById(`${user_id}dl`).disabled = false;
        }
    } catch (error) {
        console.error("Error in liked function:", error);
        // Handle error appropriately
    }
}

async function change_button_color(user_id) {
  
    let result =   await check_like(user_id);
   
    if (result == false) // if the post not already liked by the user then like it and change to color to like.
    {
  
      document.getElementById(`${user_id}l`).style.color = "blue" 
    }
    
  }