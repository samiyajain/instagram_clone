import { useEffect, useState } from "react";
import api from "../api";

//feed
function Feed() {
    const [posts, setPosts] = useState([]);


  useEffect(() => {
   const user = localStorage.getItem("user");
   api.get(`feed/${user}/`).then(res => setPosts(res.data));
}, []);


return (
   <div>
     {posts.map(p => (
       <div key={p.id}>
         <img src={p.image_url} width="200" />
         <p>{p.caption}</p>
         <p>Likes: {p.likes}</p>
       </div>
      ))}
    </div>
);
}


export default Feed;