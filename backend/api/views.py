from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import FACTS, CATEGORIES, next_id

def get_next_id():
    """Get the next available ID for new facts"""
    global next_id
    current_id = next_id
    next_id += 1
    return current_id

def facts_list(request):
    """Get all facts from the data store"""
    return JsonResponse({"facts": FACTS})

def categories_list(request):
    """Get all categories from the data store"""
    return JsonResponse({"categories": CATEGORIES})

def facts_by_category(request, category):
    """Get facts by category"""
    try:
        # Filter facts by category (case-insensitive)
        filtered_facts = [fact for fact in FACTS if fact['category'].lower() == category.lower()]
        return JsonResponse({"facts": filtered_facts})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

class CategoriesView(View):
    """Get all available categories"""
    def get(self, request):
        return JsonResponse({'categories': CATEGORIES})

class ApiRootView(View):
    """API root endpoint"""
    def get(self, request):
        return JsonResponse({
            'message': 'Facts Hub API',
            'version': '1.0.0',
            'endpoints': {
                'categories': '/api/categories/',
                'facts': '/api/facts/',
                'fact_detail': '/api/facts/{id}/',
                'add_fact': '/api/facts/add/'
            }
        })

@method_decorator(csrf_exempt, name='dispatch')
class FactsView(View):
    """Handle facts operations"""

    def get(self, request):
        """Get all facts or facts by category"""
        category = request.GET.get('category')
        
        if category:
            # Filter facts by category
            filtered_facts = [fact for fact in FACTS if fact['category'].lower() == category.lower()]
            return JsonResponse({'facts': filtered_facts})
        else:
            # Return all facts
            return JsonResponse({'facts': FACTS})

@method_decorator(csrf_exempt, name='dispatch')
class FactDetailView(View):
    """Handle individual fact operations"""
    
    def get(self, request, fact_id):
        """Get fact by ID"""
        try:
            fact_id = int(fact_id)
            fact = next((fact for fact in FACTS if fact['id'] == fact_id), None)
            
            if fact:
                return JsonResponse({'fact': fact})
            else:
                return JsonResponse({'error': 'Fact not found'}, status=404)
                
        except ValueError:
            return JsonResponse({'error': 'Invalid fact ID'}, status=400)
    
    @method_decorator(csrf_exempt)
    def delete(self, request, fact_id):
        """Delete a fact by ID"""
        try:
            fact_id = int(fact_id)
            global FACTS
            fact = next((fact for fact in FACTS if fact['id'] == fact_id), None)
            
            if fact:
                FACTS = [f for f in FACTS if f['id'] != fact_id]
                return JsonResponse({'message': 'Fact deleted successfully'})
            else:
                return JsonResponse({'error': 'Fact not found'}, status=404)
                
        except ValueError:
            return JsonResponse({'error': 'Invalid fact ID'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class AddFactView(View):
    """Handle adding new facts"""
    
    def get(self, request):
        """Return error for GET requests to add endpoint"""
        return JsonResponse({'error': 'Use POST method to add facts'}, status=405)
    
    @method_decorator(csrf_exempt)
    def post(self, request):
        """Add a new fact"""
        try:
            data = json.loads(request.body)
            
            # Validate required fields
            required_fields = ['title', 'content', 'category']
            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f'Missing required field: {field}'}, status=400)
            
            # Validate category
            if data['category'] not in CATEGORIES:
                return JsonResponse({'error': 'Invalid category'}, status=400)
            
            # Create new fact
            new_fact = {
                'id': get_next_id(),
                'title': data['title'],
                'content': data['content'],
                'category': data['category'],
                'created_at': '2024-01-01T10:00:00Z'  # Simplified for demo
            }
            
            FACTS.append(new_fact)
            return JsonResponse({'fact': new_fact}, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
