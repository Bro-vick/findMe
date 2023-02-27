import React, { useState } from "react";
import styled from "styled-components";

const FormContainer = styled.div`
  max-width: 500px;
  margin: 0 auto;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
`;

const InputLabel = styled.label`
  margin-bottom: 5px;
`;

const Input = styled.input`
  margin-bottom: 15px;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
`;

const Textarea = styled.textarea`
  margin-bottom: 15px;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
`;

const Button = styled.button`
  background-color: #0077cc;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;

  &:hover {
    background-color: #005fa3;
  }
`;

const ImageInputLabel = styled.label`
  display: block;
  margin-bottom: 5px;
`;

const ImageInput = styled.input`
  margin-bottom: 15px;
`;

export default function ProfilePage() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [bio, setBio] = useState("");
  const [profilePicture, setProfilePicture] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <div>
      <h1>Create your Profile Page</h1>

      <FormContainer>
        <Form onSubmit={handleSubmit}>
          <ImageInputLabel htmlFor="profile-picture">
            Profile Picture:
          </ImageInputLabel>
          <ImageInput
            type="file"
            id="profile-picture"
            onChange={(e) => setProfilePicture(e.target.files[0])}
          />

          <InputLabel htmlFor="username">Username:</InputLabel>
          <Input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <InputLabel htmlFor="email">Email:</InputLabel>
          <Input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <InputLabel htmlFor="bio">Bio:</InputLabel>
          <Textarea
            id="bio"
            value={bio}
            onChange={(e) => setBio(e.target.value)}
          ></Textarea>

          <Button type="submit">Save Changes</Button>
        </Form>
      </FormContainer>

      {submitted && (
        <div>
          <h2>Profile Information</h2>
          {profilePicture && (
            <img src={URL.createObjectURL(profilePicture)} alt="Profile" />
          )}
          <p>Username: {username}</p>
          <p>Email: {email}</p>
          <p>Bio: {bio}</p>
        </div>
      )}
    </div>
  );
}

