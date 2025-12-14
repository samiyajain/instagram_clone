import api from "../api";

//login
function Login() {
  const login = async () => {
  const res = await api.post("login/", {
     email: "test@gmail.com",
     password: "1234"
   });


    localStorage.setItem("user", res.data.token);
    window.location.href = "/feed";
 };


  return <button onClick={login}>Login</button>;
}


export default Login;