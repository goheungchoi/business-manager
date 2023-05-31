import { useMutation, useQuery, gql } from "@apollo/client"


const LOGIN_MUTATION = gql`
  mutation Login($username: String!, $password: String!) {
    login(username: $username, password: $password) {
      user {
        id
        username
      }
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
  let input = {}
  const [login, { error, reset }] = useMutation(LOGIN_MUTATION);

  return (
    <div>
      <form
        onSubmit={e => {
          e.preventDefault();
          login({ variables: 
            { 
              username: input.username.value,
              password: input.password.value,
            } 
          });
          input.username.value = "";
          input.password.value = "";
        }}
      >
        <input
          ref={node => {
            input.username = node;
          }}
          placeholder="Username"
        />
        <input
          ref={node => {
            input.password = node;
          }}
          placeholder="Password"
          type="password"
        />
        
        <button type="submit">Login</button>
      </form>
      {
        error &&
        <LoginFailedMessageWindow
          message={error.message}
          onDismiss={() => reset()}
        />
      }
    </div>
  )
}

export default LogInForm;
