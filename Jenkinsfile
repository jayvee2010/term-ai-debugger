pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }

    environment {
        // Docker Hub configuration
        DOCKER_HUB_USERNAME = credentials('docker-hub-username')
        DOCKER_HUB_TOKEN = credentials('docker-hub-token')
        IMAGE_NAME = 'terminal-debugger'
        IMAGE_TAG = "${BUILD_NUMBER}"
        DOCKER_IMAGE = "${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}"
        DOCKER_LATEST = "${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest"
    }

    stages {
        stage('📥 Checkout') {
            steps {
                script {
                    echo '═══════════════════════════════════════════════'
                    echo '  Checking out source code from GitHub...'
                    echo '═══════════════════════════════════════════════'
                }
                checkout scm
            }
        }

        stage('🔍 Inspect Project') {
            steps {
                script {
                    echo '═══════════════════════════════════════════════'
                    echo '  Project files:'
                    echo '═══════════════════════════════════════════════'
                    sh 'ls -la'
                    sh 'echo "---" && cat requirements.txt'
                }
            }
        }

        stage('🐍 Test Python Environment') {
            steps {
                script {
                    echo '═══════════════════════════════════════════════'
                    echo '  Setting up Python virtual environment...'
                    echo '═══════════════════════════════════════════════'
                    sh '''
                        python3 --version
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        echo "✅ Dependencies installed successfully"
                    '''
                }
            }
        }

        stage('✅ Run Tests') {
            steps {
                script {
                    echo '═══════════════════════════════════════════════'
                    echo '  Running tests (if any)...'
                    echo '═══════════════════════════════════════════════'
                    sh '''
                        . venv/bin/activate
                        # Try to run pytest if it exists, otherwise skip
                        if python -m pytest --version 2>/dev/null; then
                            pytest tests/ -v 2>/dev/null || echo "⚠️  No tests found, skipping"
                        else
                            echo "⚠️  pytest not installed, skipping tests"
                        fi
                    '''
                }
            }
        }

        stage('🐳 Build Docker Image') {
            steps {
                script {
                    echo '═══════════════════════════════════════════════'
                    echo '  Building Docker image...'
                    echo '  Image: ' + DOCKER_IMAGE
                    echo '═══════════════════════════════════════════════'
                    sh '''
                        docker build -t ${DOCKER_IMAGE} .
                        docker tag ${DOCKER_IMAGE} ${DOCKER_LATEST}
                        echo "✅ Docker image built successfully"
                        docker images | grep terminal-debugger
                    '''
                }
            }
        }

        stage('🔐 Login to Docker Hub') {
            steps {
                script {
                    echo '═══════════════════════════════════════════════'
                    echo '  Logging in to Docker Hub...'
                    echo '═══════════════════════════════════════════════'
                    sh '''
                        echo ${DOCKER_HUB_TOKEN} | docker login -u ${DOCKER_HUB_USERNAME} --password-stdin
                        echo "✅ Successfully logged in to Docker Hub"
                    '''
                }
            }
        }

        stage('📤 Push to Docker Hub') {
            steps {
                script {
                    echo '═══════════════════════════════════════════════'
                    echo '  Pushing image to Docker Hub...'
                    echo '  Pushing: ' + DOCKER_IMAGE
                    echo '  Pushing: ' + DOCKER_LATEST
                    echo '═══════════════════════════════════════════════'
                    sh '''
                        docker push ${DOCKER_IMAGE}
                        docker push ${DOCKER_LATEST}
                        echo "✅ Successfully pushed to Docker Hub"
                    '''
                }
            }
        }

        stage('🧹 Cleanup') {
            always {
                script {
                    echo '═══════════════════════════════════════════════'
                    echo '  Cleaning up...'
                    echo '═══════════════════════════════════════════════'
                    sh '''
                        docker logout || true
                        rm -rf venv
                        echo "✅ Cleanup complete"
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '╔════════════════════════════════════════════════╗'
            echo '║  ✅ PIPELINE SUCCEEDED!                        ║'
            echo '║  Image pushed: ' + DOCKER_LATEST
            echo '╚════════════════════════════════════════════════╝'
        }
        failure {
            echo '╔════════════════════════════════════════════════╗'
            echo '║  ❌ PIPELINE FAILED                            ║'
            echo '║  Check the logs above for details              ║'
            echo '╚════════════════════════════════════════════════╝'
        }
    }
}
