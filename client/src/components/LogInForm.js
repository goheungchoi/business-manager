import { useMutation, useQuery, gql } from "@apollo/client"
import { useState, useEffect } from "react"
import { useNavigate } from 'react-router-dom'

const LOGIN_MUTATION = gql`
  mutation Login($username: String!, $password: String!) {
    login(username: $username, password: $password) {
      user {
        id
        firstName
        lastName
        username
        department
        title
        role
        email
        emailSignature
        phone
        mobile
        homePhone
        manager {
          id
        }
        lastLogin
      }
      errorMessage
    }
  }
`;


function LoginFailedMessageWindow({ message, onDismiss }) {
  return (
    <div style={{ 
      position: "absolute", 
      top: "50%", 
      left: "50%", 
      transform: "translate(-50%, -50%)",
      backgroundColor: "white",
      border: "1px solid black",
      padding: "20px",
      zIndex: 100,
    }}>
      <h2>Login Failed</h2>
      <p>{message}</p>
      <button onClick={onDismiss}>Close</button>
    </div>
  );
}

function LogInForm() {
  const [input, setInput] = useState({
    username: "",
    password: "",
  })
  const [login, { data, error, reset }] = useMutation(LOGIN_MUTATION);
  const navigate = useNavigate();

  return (
    <div>
      <form
        onSubmit={e => {
          e.preventDefault();
          login({ variables: 
            { 
              username: input.username,
              password: input.password,
            } 
          }).then(request => {
            const id = request.data.login.user.id;
            console.log(id);

            localStorage.setItem('id', id)

            navigate('/user/' + id);
          });

          setInput({
            username: "",
            password: "",
          });
        }}
      >
        <input
          value={input.username}
          onChange={e=>setInput({
            ...input,
            username: e.target.value
          })}
          placeholder="Username"
        />
        <input
          value={input.password}
          onChange={e=>setInput({
            ...input,
            password: e.target.value
          })}
          placeholder="Password"
          type="password"
        />
        
        <button type="submit">Login</button>
      </form>
      {
        (error || (data && data.login.error_message)) &&
        <LoginFailedMessageWindow
          message={error ? error.message : data.login.error_message}
          onDismiss={() => reset()}
        />
      }
    </div>
  )
}

export default LogInForm;
