from project import create_app

if __name__ == '__main__':
  app = create_app()
  # app.config['TEMPLATES_AUTO_RELOAD'] = True
  # app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
  app.run(host = '0.0.0.0', port = 8000, debug=True)
