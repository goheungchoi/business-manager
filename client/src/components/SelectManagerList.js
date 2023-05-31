import { useQuery, gql } from "@apollo/client";

const GET_USERS = gql`
  query GetUsers($role: String!) {
    users(role: $role) {
      id
      firstName
      lastName
      username
      department
    }
  }
`;

function SelectManagerList({ handleSelectManager }) {
  const { loading, error, data } = useQuery(GET_USERS, {
    variables: { role: "MANAGER" }
  });

  if (loading) return <select></select>;
  if (error) return <section><option></option></section>;

  return (
    <div>
      <label for="managers">Find your manager:</label>
      <select 
        name="manager" 
        id="select-manager"
        onChange={e => handleSelectManager(e)}
      >
        <option
          value="none" 
          selected 
          disabled 
          hidden
        >
          Select Manager
        </option>
        {data.users.map((user) => (
          <option value={user.id}>
            {user.firstName} {user.lastName} : {user.department}
          </option>
        ))}
      </select>
    </div>
  )
}

export default SelectManagerList;
