import React, { useEffect } from 'react'
import { useCookies, CookiesProvider } from 'react-cookie'
import PropTypes from 'prop-types'
import { Form, Icon, Input, Button } from 'antd'
import axios from 'axios'
import './Login.css'

function Login(props) {
  // eslint-disable-next-line no-unused-vars
  const [cookie, setCookie] = useCookies(['login'])

  const hasErrors = (fieldsError) => {
    return Object.keys(fieldsError).some(field => fieldsError[field])
  }

  const handleSubmit = e => {
    e.preventDefault()
    props.form.validateFields((err, values) => {
      if (!err) {
        axios.post('/login', {password: values}).then(({data}) => {
          if (data.success) {
            setCookie('login', data.token, {maxAge: data.maxAge, expires: data.expires})
          } else {
            console.error(err)
          }
        }).catch((err) => {
          console.error(err)
        })
      }
    })
  }

  const { getFieldDecorator, getFieldsError, getFieldError, isFieldTouched } = props.form  
  const passwordError = isFieldTouched('password') && getFieldError('password')

  useEffect(() => {
    props.form.validateFields();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  return (
    <CookiesProvider>
      <Form layout="inline" onSubmit={handleSubmit}>
        <Form.Item validateStatus={passwordError ? 'error' : ''} help={passwordError || ''}>
          {getFieldDecorator('password', {
            rules: [{ required: true, message: 'Please input your Password!' }]
          })(
            <Input
              prefix={<Icon type="lock" style={{ color: 'rgba(0,0,0,.25)' }} />}
              type="password"
              placeholder="Password" />
          )}
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit" disabled={hasErrors(getFieldsError())}>
            Log in
          </Button>
        </Form.Item>
      </Form>
    </CookiesProvider>
  )
}

Login.propTypes = {
  form: PropTypes.object.isRequired
};

const LoginForm = Form.create({ name: 'login' })(Login)

export default LoginForm
