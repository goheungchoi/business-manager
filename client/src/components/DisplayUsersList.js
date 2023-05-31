import { useQuery, gql } from "@apollo/client";
import { Link } from "react-router-dom";

const GET_USERS = gql`
  query GetUsers {
    users {
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

function UsersList() {
  const { loading, error, data } = useQuery(GET_USERS);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error : {error.message}</p>;

  return (
    <div>
      <h2>User List</h2>
      <ol>
      {
        data.users.map((user) => (
          <li>
            <div key={user.username}>
              <h3>{user.firstName} {user.lastName}</h3>
              <p>Department: {user.department}</p>
              <Link to={`/admin/${user.id}`} >
                <button type="button">
                  Details
                </button>
              </Link>
              {/* <p>Title: {user.title}</p>
              <p>Role: {user.role}</p>
              <p>Email: {user.email}</p>
              <p>Phone: {user.phone}</p>
              <p>Mobile: {user.mobile}</p>
              <p>Home Phone: {user.home_phone}</p> */}
            </div>
          </li>
        ))
      }
      </ol>
      
    </div>
  );
}

export default UsersList;
