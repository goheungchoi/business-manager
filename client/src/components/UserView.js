import { useEffect, useState } from "react";
import { useQuery, gql } from "@apollo/client";
import { useParams } from "react-router-dom";

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
      emailSignature
      phone
      mobile
      homePhone
      manager {
        firstName
        lastName
        department
        email
        phone
      }
      lastLogin
    }
  }
`;


function UserView() {
  let { id } = useParams();
  const [isAuth, setIsAuth] = useState(false);
  const {loading, error, data} = useQuery(GET_USER, {
    variables: { id }
  });

  useEffect(() => {
    if (localStorage.getItem('access') === null) {
      window.location.href = '/login'
    } else {
      setIsAuth(true);
    }

    console.log(data);
  }, [isAuth]);

  return (
    !isAuth ? null :
    <div>
      Hello! 
      {loading && <div>Loading...</div>}
      {error ? <div>Error : {error.message}</div> :
        <div>
          <h3>{data.firstName} {data.lastName}</h3>
          <p>Department: {data.department}</p>
          <p>Title: {data.title}</p>
          <p>Role: {data.role}</p>
          <p>Email: {data.email}</p>
          <p>Phone: {data.phone}</p>
          <p>Mobile: {data.mobile}</p>
          <p>Home Phone: {data.homePhone}</p>
          <p>Last Login: {data.lastLogin}</p>

          <h2>Manager: {data.manager.firstName} {data.user.manager.lastName}</h2>
          <p>Department: {data.manager.department}</p>
          <p>Email: {data.manager.email}</p>
          <p>Phone: {data.manager.phone}</p>
        </div>
      }
      
    </div>
  )
}

export default UserView;
