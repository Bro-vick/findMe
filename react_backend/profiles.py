from flask_restx import Namespace, Resource, fields
from models import Profile
from flask_jwt_extended import jwt_required
from flask import request


profile_ns=Namespace('profile', description="A namespace for profiles")

profile_model=profile_ns.model(
    "Profile",
    {
        "id":fields.Integer(),
        "username":fields.String(),
        "user_bio":fields.String(),
        "picture_url":fields.String(),
        "twitter":fields.String(),
        "github":fields.String(),
        "linkedin":fields.String()
    },
)


@profile_ns.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello world"}



@profile_ns.route("/profiles")
class ProfilesResource(Resource):
    @profile_ns.marshal_list_with(profile_model)
    def get(self):
        """Get all profiles"""
        profiles = Profile.query.all()
        return profiles

    @profile_ns.marshal_with(profile_model)
    @profile_ns.expect(profile_model)
    @jwt_required()
    def post(self):
        """Create a new profile"""
        data=request.get_json()
        
        new_profile=Profile(
            username=data.get('username'),
            user_bio=data.get('user_bio'),
            picture_url=data.get('picture_url'),
            twitter=data.get('twitter'),
            github=data.get('github'),
            linkedin=data.get('linkedin')
        )

        new_profile.save()
        return new_profile,201


@profile_ns.route('/profile/<int:id>')
class ProfileResource(Resource):
    @profile_ns.marshal_with(profile_model)
    def get(self,id):
        """Get a profile by id"""
        profile=Profile.query.get_or_404(id)
        return profile

    @profile_ns.marshal_with(profile_model)
    @jwt_required()
    def put(self,id):
        """Update a profile by id"""
        profile_to_update=Profile.query.get_or_404(id)
        data=request.get_json()
        profile_to_update.update(
            data.get('username'),
            data.get('user_bio'),
            data.get('picture_url'),
            data.get('twitter'),
            data.get('github'),
            data.get('linkedin')
        )
        return profile_to_update

    @profile_ns.marshal_with(profile_model)
    @jwt_required()
    def delete(self,id):
        """Delete profile by id"""
        profile_to_delete=Profile.query.get_or_404(id)
        profile_to_delete.delete()
        return profile_to_delete