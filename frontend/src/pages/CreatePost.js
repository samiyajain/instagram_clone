import api from "../api";


function CreatePost() {
  const create = async () => {
    await api.post("post/", {
       user_id: localStorage.getItem("user"),
       image_url: "https://picsum.photos/200",
    caption: "My first post"
     });
 };


  return <button onClick={create}>Create Post</button>;
}


export default CreatePost;