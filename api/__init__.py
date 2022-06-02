"""
Welcome to the documentation for the DartsPlus API!

This project is written in Python, with the
[Flask](https://flask.palletsprojects.com/) web framework. This documentation
is generated automatically using
the [APIFairy](https://github.com/miguelgrinberg/apifairy) Flask extension.

## Configuration

If you are running DartsPlus API yourself while developing your front end,
there are a number of environment variables that you can set to configure its
behavior. The variables can be defined directly in the environment or in a
`.env` file in the project directory. The following table lists all the
environment variables that are currently used:

| Environment Variable | Default | Description |
| - | - | - |
| `SECRET_KEY` | `dartsplus` | A secret key used when signing tokens. |
| `DATABASE_URL`  | `sqlite:///db.sqlite` | The database URL, as defined by the [SQLAlchemy](https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls) framework. |
| `SQL_ECHO` | not defined | Whether to echo SQL statements to the console for debugging purposes. |
| `DISABLE_AUTH` | not defined | Whether to disable authentication. When running with authentication disabled, the user is assumed to be logged as the first user in the database. |
| `ACCESS_TOKEN_EXPIRATION` | `60` (1 hour) | The number of minutes an access token is valid for. |
| `REFRESH_TOKEN_EXPIRATION` | `1440` (24 hours) | The number of minutes a refresh token is valid for. |
| `RESET_TOKEN_EXPIRATION` | `15` (15 minutes) | The number of minutes a reset token is valid for. |
| `DOCS_UI` | `elements` | The UI library to use for the documentation. Allowed values are `swagger_ui`, `redoc`, `rapidoc` and `elements`. |

## Authentication

The authentication flow for this API is based on *access* and *refresh*
tokens.

To obtain an access and refresh token pair, the client must send a `POST`
request to the `/api/tokens` endpoint, passing the username and password of
the user in a `Authorization` header, according to HTTP Basic Authentication
scheme.

Most endpoints in this API are authenticated with the access token, passed
also in the `Authorization` header, but this time using the `Bearer` scheme.

Access tokens are valid for one hour (by default) from the time they are
issued. When the access token is expired, the client can renew it using the
refresh token. For this, the client must send a `PUT` request to the
`/api/tokens` endpoint, passing both the expired access token and the still
valid refresh token in the body of the request. The response to this request
will include a new token pair. Refresh tokens have a default validity period of
24 hours, and can only be used to renew the access token that was returned with
it.

A refreshed access token can be used exactly as an originally issued one, but
refreshed tokens are restricted from performance sensitive operations such as
changing the user's password for security purposes.

All authentication failures are handled with a `401` status code in the
response.

### Password Resets

This API also supports a password reset flow, to help users who forget their
passwords. To issue a password request, the client must send a `POST` request
to `/api/tokens/reset`, passing the user's email in the body of the request.
The user will receive a password reset link by email, which is the request's
[Referrer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer)
URL, with an added `token` query string argument set to an email reset token,
with a validity of 15 minutes.

When the user clicks on the password reset link, the client application must
capture the `token` query string argument and send it in a `PUT` request to
`/api/tokens/reset`, along with the new password chosen by the user.

## Errors

All errors returned by this API use the following JSON structure:

```json
{
    "code": <numeric error code>,
    "message": <short error message>,
    "description": <longer error description>,
}
```

In the case of schema validation errors, an `errors` property is also returned,
containing a detailed list of validation errors found in the submitted request:

```json
{
    "code": <error code>,
    "message": <error message>,
    "description": <error description>,
    "errors": [ <error details>, ... ]
}
```

"""  # noqa: E501

from api.app import create_app, db, ma  # noqa: F401
