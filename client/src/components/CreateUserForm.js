import { useMutation, useQuery, gql } from "@apollo/client";
import { useState, createRef } from "react";
import SelectManagerList from "./SelectManagerList";

const CREATE_USER = gql`
  mutation CreateUser($input: UserInput!) {
    createUser(input: $input) {
      user {
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
    }
  }
`;

const GET_USER = gql`
  query GerUser($id: ID!) {
    user(id: $id) {
      id
      firstName
      lastName
      username
      department
      title
      role
      email
      phone
      mobile
      homePhone
    }
  }
`;

function GetManager({ id }) {
  const {loading, error, data} = useQuery(GET_USER, {
    variables: { id }
  });

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error : {error.message}</div>;

  return (
    <div>
      <h3>{data.user.first_name} {data.user.last_name}</h3>
      <p>Department: {data.user.department}</p>
      <p>Title: {data.user.title}</p>
      <p>Role: {data.user.role}</p>
      <p>Email: {data.user.email}</p>
      <p>Phone: {data.user.phone}</p>
      <p>Mobile: {data.user.mobile}</p>
      <p>Home Phone: {data.user.home_phone}</p>
    </div>
  )
}

function CreateUserForm() {
  const [input, setInput] = useState({
    first_name: "",
    last_name: "",
    username: "",
    department: "",
    title: "",
    email: "",
    phone: "",
    mobile: "",
    home_phone: "",
  });

  const buildEmailSign = () => {
    return (
      "<i>" + input.first_name + 
      input.last_name + "<\i>" +
      "<br><\br><br><\br>" +
      + input.department + "<br><\br>"
      + input.title +"<br><\br>"
      + "Contact: <br><\br>" +
      + input.email + "<br><\br>"
      + input.phone + "<br><\br>"
    )
  }
  
  const [role, setRole] = useState("OTHER");
  const [managerId, setManagerId] = useState()
  const [password, setPassword] = useState('');
  const [passwordConfirm, setPasswordConfirm] = useState('');
  const [createUser, { error, loading, data }] = useMutation(CREATE_USER);

  function onSelectManager(e) {
    setManagerId(e.target.value);
  }

  return (
    <div>
      <form
        onSubmit={e => {
          e.preventDefault();
          if (password !== passwordConfirm) {
            alert("Passwords do not match!")
            return;
          }

          const emailSign = buildEmailSign();

          console.log(input);

          createUser({ 
            variables: { 
              input: {
                firstName: input.first_name,
                lastName: input.last_name,
                username: input.username,
                password: password,
                department: input.department,
                title: input.title,
                role: role,
                email: input.email,
                emailSignature: emailSign,
                phone: input.phone,
                mobile: input.mobile,
                homePhone: input.home_phone,
                manager: managerId,
              } 
            } 
          });
          setInput({
            first_name: "",
            last_name: "",
            username: "",
            department: "",
            title: "",
            email: "",
            phone: "",
            mobile: "",
            home_phone: "",
          });
        }}
      >
        <input
          value={input.first_name}
          onChange={e=>setInput({
            ...input,
            first_name: e.target.value
          })}
          placeholder="First Name"
        />
        <input
          value={input.last_name}
          onChange={e=>setInput({
            ...input,
            last_name: e.target.value
          })}
          placeholder="Last Name"
        />
        <input
          value={input.username}
          onChange={e=>setInput({
            ...input,
            username: e.target.value
          })}
          placeholder="Username"
        />
        <input
          value={password}
          onChange={e =>
            setPassword(e.target.value)
          }
          placeholder="Password"
          type="password"
        />
        <input
          value={passwordConfirm}
          onChange={e => 
            setPasswordConfirm(e.target.value)
          }
          placeholder="Confirm"
          type="password"
        />
        { 
          password === passwordConfirm ? null :
          "Passwords didn't match. Try again."
        }
        <input
          value={input.department}
          onChange={e=>setInput({
            ...input,
            department: e.target.value
          })}
          placeholder="Department"
        />
        <input
          value={input.title}
          onChange={e=>setInput({
            ...input,
            title: e.target.value
          })}
          placeholder="Title"
        />
        <select
          onChange={e=>
            setRole(e.target.value)
          }
        >
          <option 
            value="none" 
            selected 
            disabled 
            hidden
          >
            Select your role
          </option>
          <option value="MANAGER">Manager</option>
          <option value="EMPLOYEE">Employee</option>
          <option value="ADMIN">Admin</option>
          <option value="OTHER">Other</option>
        </select>
        <input
          value={input.email}
          onChange={e=>setInput({
            ...input,
            email: e.target.value
          })}
          placeholder="Email"
          type="email"
        />
        <input
          value={input.phone}
          onChange={e=>setInput({
            ...input,
            phone: e.target.value
          })}
          placeholder="Phone"
        />
        <input
          value={input.mobile}
          onChange={e=>setInput({
            ...input,
            mobile: e.target.value
          })}
          placeholder="Mobile"
        />
        <input
          value={input.home_phone}
          onChange={e=>setInput({
            ...input,
            home_phone: e.target.value
          })}
          placeholder="Home Phone"
        />

        <SelectManagerList 
          handleSelectManager={onSelectManager}
        />

        { managerId ? <GetManager id={managerId} /> : null}
        
        <button type="submit">Create User</button>
      </form>
    </div>
  );
}

export default CreateUserForm;
